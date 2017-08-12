'''
Testing the BinaryTree module
Roman Yasinovskyy, 2017
See https://stackoverflow.com/a/31281467 for testing output
'''

#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from io import StringIO
from adjacency_graph import Graph


class TestAdjacencyGraphMethods(unittest.TestCase):
    '''Testing the Binary Heap module'''

    def setUp(self):
        '''Setting up'''
        self._graph = Graph()

    def testMakeGraph(self):
        '''Testing_make_graph'''
        gFile = open("test.dat")
        for line in gFile:
            fVertex, tVertex = line.split('|')
            fVertex = int(fVertex)
            tVertex = int(tVertex)
            self._graph.addEdge(fVertex,tVertex)
        for i in self._graph:
            adj = i.getAdj()
            for k in adj:
                print(i, k)

    def tearDown(self):
        '''Tearing down'''
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
