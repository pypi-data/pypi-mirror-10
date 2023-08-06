import collections
from itertools import izip
from Queue import PriorityQueue

import numpy
from chainer import Function

class TreeParser(object):
    def __init__(self):
        self.next_id = 0

    def size(self):
        return self.next_id

    def get_paths(self):
        return self.paths

    def get_codes(self):
        return self.codes

    def parse(self, tree):
        self.next_id = 0
        self.path = []
        self.code = []
        self.paths = {}
        self.codes = {}
        self._parse(tree)

        assert(len(self.path) == 0)
        assert(len(self.code) == 0)
        assert(len(self.paths) == len(self.codes))

    def _parse(self, node):
        if isinstance(node, tuple):
            # internal node
            if len(node) != 2:
                raise ValueError('All internal nodes must have two child nodes')
            left, right = node
            self.path.append(self.next_id)
            self.next_id += 1
            self.code.append(1.0)
            self._parse(left)

            self.code[-1] = -1.0
            self._parse(right)

            self.path.pop()
            self.code.pop()

        else:
            # leaf node
            self.paths[node] = numpy.array(self.path).astype(numpy.int32)
            self.codes[node] = numpy.array(self.code).astype(numpy.float32)


class BinaryHierarchicalSoftmax(Function):
    """Implementation of hierarchical softmax (HSM)."""

    parameter_names = ('W',)
    gradient_names = ('gW',)

    def __init__(self, in_size, tree):
        """Initilizes :class:`BinaryHierarchicalSoftmax` by a given binary tree.

        Args:
            in_size (int): Dimension of input vectors.
            tree: A binary tree made with tuples like `((1, 2), 3)`.
        """
        parser = TreeParser()
        parser.parse(tree)
        self.paths = parser.get_paths()
        self.codes = parser.get_codes()

        self.W = numpy.random.uniform(-1, 1, (parser.size(), in_size)).astype(numpy.float32)
        self.gW = numpy.zeros(self.W.shape, numpy.float32)

    def forward_cpu(self, (x, t)):
        assert x.ndim == 2 and x.dtype.kind == 'f'
        assert t.ndim == 1 and t.dtype.kind == 'i'
        assert len(x) == len(t)

        loss = 0.0
        for ix, it in izip(x, t):
            loss += self._forward_cpu_one(ix, it)
        return numpy.array([loss]),

    def _forward_cpu_one(self, x, t):
        assert t in self.paths

        w = self.W[self.paths[t]]
        wxy = w.dot(x) * self.codes[t]
        loss = numpy.logaddexp(0, -wxy)  # == log(1 + exp(-wxy))
        return numpy.sum(loss)

    def backward_cpu(self, (x, t), (gloss,)):
        gx = numpy.empty_like(x)
        for i, (ix, it) in enumerate(izip(x, t)):
            gx[i] = self._backward_cpu_one(ix, it, gloss[0])
        return gx, None

    def _backward_cpu_one(self, x, t, gloss):
        path = self.paths[t]
        w = self.W[path]
        wxy = w.dot(x) * self.codes[t]
        g = -gloss * self.codes[t] / (1.0 + numpy.exp(wxy))
        gx = g.dot(w)
        gw = g.reshape((g.shape[0], 1)).dot(x.reshape(1, x.shape[0]))
        self.gW[path] += gw
        return gx


def create_huffman_tree(word_counts):
    """Make a huffman tree from a dictionary containing word counts.

    This method creates a binary huffman tree, that is required for
    :class:`BinaryHierarchicalSoftmax`.
    For example, ``{0: 8, 1: 5, 2: 6, 3: 4}`` is converted to
    ``((3, 1), (2, 0))``.

    Args:
        word_counts (``dict`` of ``int`` key and ``int`` or ``float`` values.): 
            Dictionary representing counts of words.

    Returns:
        Binary huffman tree with tuples and keys of ``word_coutns``.
    """
    if len(word_counts) == 0:
        raise ValueError('Empty vocabulary')

    q = PriorityQueue()
    for w, c in word_counts.iteritems():
        q.put((c, w))

    while q.qsize() >= 2:
        (count1, word1) = q.get()
        (count2, word2) = q.get()
        count = count1 + count2
        tree = (word1, word2)
        q.put((count, tree))

    return q.get()[1]

