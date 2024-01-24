# Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Thought Process and Concepts Utilized
# 1.Problem Understanding:
# -The task is to determine the maximum depth of a binary tree, where depth is defined as the number of 
# nodes along the longest path from the root node down to the farthest leaf node.
# -A binary tree is a tree data structure where each node has at most two children, referred to as the left
# child and the right child.
# -It's essential to understand that the maximum depth of the tree is determined by the deepest branch 
# (left or right) from the root node.

# 2.Algorithm Choice:
# -Recursive Depth-First Search (DFS): The choice of a recursive DFS approach is well-suited to tree 
# structures, especially for tasks like calculating depth. It naturally navigates through all possible 
# paths (left and right) from the root to the leaves, calculating depths along the way.
# -Comparative Analysis of Subtrees: The algorithm involves comparing the depths of the left and right 
# subtrees at each node and taking the larger value as the depth for that node. This comparison is key to 
# ensuring that the longest path is considered.
# -Simplicity and Elegance of Recursion: Recursive methods offer a clean and straightforward implementation
# for tree traversal problems. The base case handles the scenario of an empty tree (or leaf nodes), while 
# the recursive case handles the depth calculation by exploring each subtree.
# -Inherent Tree Structure Utilization: This approach leverages the inherent hierarchical structure of a 
# binary tree, where each subtree can be treated as a tree in itself, allowing for a divide-and-conquer 
# methodology.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        Return the maximum depth of a binary tree.
        :type root: TreeNode
        :rtype: int
        """
        # Base case: An empty tree has a depth of 0
        if root is None:
            return 0

        # Recursively find the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # The depth of the tree is the max of the depths of the subtrees, plus 1 for the root
        return max(left_depth, right_depth) + 1

### Explanation
# -Base Case: If `root` is `None`, return 0 since an empty tree has no depth.
# -Recursive Calls: For a non-empty tree, recursively call `maxDepth` on the left and right children of 
# `root`. This will return the depth of each subtree.
# -Calculating Maximum Depth: The depth of the current tree is the larger of the depths of the left and 
# right subtrees, plus one to account for the current (root) node.

### Time & Space Complexities
# -Time Complexity: O(n), where `n` is the number of nodes in the tree. This is because the algorithm must
# visit each node once to compute its depth.
# -Space Complexity: O(h), where `h` is the height of the tree. This space is used by the call stack during
# the recursion. In the worst case, if the tree is completely unbalanced, `h` can be as large as `n` (for
# a linear tree). In the best case (a balanced tree), `h` would be log(n).
        
        