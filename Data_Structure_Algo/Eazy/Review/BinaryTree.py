## Binary Tree Paths
# Given the root of a binary tree, return all root-to-leaf paths in any order. A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        root_to_leaf = []
        self.binaryTreePathsRecu(root, "", root_to_leaf)
        return root_to_leaf
        