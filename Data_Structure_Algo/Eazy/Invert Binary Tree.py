# Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.

### Thought Process and Concepts Utilized
## 1.Problem Understanding:
# -The task is to invert a binary tree, which means swapping the left and right children of every node in 
# the tree.
# -A key aspect of understanding this problem is recognizing that inverting a tree involves performing the 
# same action (child swapping) at every node, from the root down to the leaves.
# -The challenge is to implement this in a way that efficiently and correctly inverts every node in the tree, 
# regardless of its structure or size.

## 2.Algorithm Choice:
# -Recursive Approach: The choice of using recursion is driven by the inherent recursive nature of trees. 
# Each subtree of a binary tree is a tree in itself, making recursion a natural and efficient method for 
# tree manipulation tasks like inversion.
# -Simple Node Swapping: At each node in the tree, the algorithm simply swaps the left and right children. 
# This approach directly addresses the problem's requirement and is easy to implement.
# -Depth-First Traversal: The recursion effectively performs a depth-first traversal of the tree. It inverts 
# the children of a node and then recursively inverts each of those children's subtrees. This ensures that
# the entire tree is inverted by the time the recursion unwinds back to the root.
# -Base Case for Recursion: The base case for the recursion is when a node is null (indicating an empty tree
# or leaf node), at which point the recursion stops. This is essential to avoid null pointer errors and to
# ensure that the recursion terminates correctly.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Base case: if the tree is empty
        if not root:
            return None
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

## Explanation
# -Base Case: If `root` is `None`, return `None` since an empty tree is already "inverted".
# -Swapping Children: For a non-empty node, swap its left and right children.
# -Recursive Calls: Recursively call `invertTree` on both the left and right children of the current node. 
# This ensures that the entire tree is inverted.
# -Return the Root: After inverting the entire tree, return the root of the inverted tree.

## Time & Space Complexities
# -Time Complexity: O(n), where `n` is the number of nodes in the tree. Each node is visited once.
# -Space Complexity: O(h), where `h` is the height of the tree. This space is used by the call stack during
# the recursion. For a balanced tree, this would be O(log n), and for a completely unbalanced tree, it 
# would be O(n).
