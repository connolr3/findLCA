# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:28:51 2020

@author: rosie
"""
import unittest
#import findLCA

from findLCA import findLCA
from findLCA import Node

class TestLCA(unittest.TestCase):

    def test_Tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(2, findLCA(root, 4, 5), "3 should be LCA of 6 & 7")
        self.assertEqual(3, findLCA(root, 6, 7), "3 should be LCA of 6 & 7")
              
    def test_One_Null_Node(self):
        root = Node(1)
        root.left = Node(2)
        self.assertEqual(-1, findLCA(root, 1, 3), "Should be -1 one node not present")
        
    def test_Tree_No_Nodes(self):
        root = None
        self.assertEqual(-1, findLCA(root, 6, 7), "Should be -1 for empty tree")
        
    def test_Two_Null_Node(self):
        root = Node(1)
        root.left = Node(2)
        self.assertEqual(-1, findLCA(root, 7, 11), "Should be -1 two nodes not present")
        
    def test_None_Node(self):
        root = Node(1)
        root.left = Node(2)
        self.assertEqual(-1, findLCA(root, None, 2), "Should be -1 as one node is None type")
        self.assertEqual(-1, findLCA(None, 1, 2), "Should be -1 as one node is None type")
        self.assertEqual(-1, findLCA(root, None, None), "Should be -1 as two nodes are None type")
        self.assertEqual(-1, findLCA(None, None, None), "Should be -1 as two nodes and root are None type")
        
    def test_LCA_is_self_nodes(self):
        root = Node(1)
        root.left = Node(2)
        self.assertEqual(2, findLCA(root,2, 2), "2 should be LCA of node 2 and 2")
        self.assertEqual(1, findLCA(root,1,1), "root should be LCA of root and root")
        self.assertEqual(1, findLCA(root,1,2), "root should be LCA of root and and other")
        
    def test_same_node_twice(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left=Node(6)
        self.assertEqual(2, findLCA(root,6, 5), "2 should be LCA of node 5 and leftmost occurenct of 6")
       
    def test_Tree_one_node(self):
        root = Node(1)
        self.assertEqual(1, findLCA(root, 1,1), "1 should be the root of 1 and 1")
        
    def test_double_Tree(self):
        root = Node(1.1)
        root.left = Node(2.2)
        root.right = Node(3.45)
        root.left.left = Node(4.54)
        root.left.right = Node(5.75)
        root.right.left = Node(6.65)
        root.right.right = Node(7.65)
        self.assertEqual(1.1, findLCA(root, 4.54, 7.65), "3 should be LCA of 6 & 7")
        
    def test_String_Tree(self):
        root = Node("root")
        root.left = Node("root - left")
        root.right = Node("root - right")
        root.left.left = Node("root - left - left")
        self.assertEqual("root - left", findLCA(root, "root - left", "root - left - left"), "root left should be LCA of root left and root left left")
       
    def test_char_Tree(self):
        root = Node('a')
        root.left = Node('b')
        root.right = Node('c')
        root.left.left = Node('d')
        self.assertEqual('a', findLCA(root,'b','c'), "a should be LCA of b and c")
       
if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    