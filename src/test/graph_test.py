import sys
sys.path.append('..')
import unittest
from collections import Counter
import numpy as np
from graph import Graph

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

class GraphTest(unittest.TestCase):
    def setUp(self):
        self.trigrams = ["a:a:a", "a:a:a", "c:c:c", "h:h:h", "a:j:l", "g:g:g"]
        self.labels = ["a", None, "c", "s", None, None]
        self.pmi_vectors = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0.9, 1, 1, 0.9],
            [1, 1, 10, 1, 10, 1, 10, 1, 10],
            [1, 3, 10, 1, 3, 1, 0, 1, 10],
            [10, 1, 10, 1, 5, 0, 10, 1, 10],
            [10, 1, 14, 1, 4, 100, 0, 1, 1]
        ]
        self.graph = Graph(self.trigrams, self.pmi_vectors, 3)

    def test_number_of_edge(self):
        print('s')

if __name__ == '__main__':
    unittest.main()
