# Lowest Common Ancestor of a Binary Search Tree
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q 
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Constraints:
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.

# 1. Problem Understanding:
#- The objective is to find the lowest common ancestor (LCA) of two given nodes in a binary search tree (BST).
#- The LCA is defined as the lowest node in the tree that has both given nodes as descendants (including the 
# possibility of a node being a descendant of itself).
#- Understanding the properties of a BST is crucial: for any node, all nodes in its left subtree are smaller, and 
# all nodes in its right subtree are larger.

# 2. Algorithm Choice:
#- Iterative Tree Traversal: Chosen for its efficiency, this approach leverages BST properties to navigate towards 
# the LCA.
#- Decision-Based Traversal: Since BSTs are ordered, we can decide whether to move left or right at each node, which 
# simplifies finding the LCA. If both target nodes are smaller than the current node, we move left; if larger, we 
# move right.
#- First Split Point: The first point where the paths to `p` and `q` diverge is the LCA. This can also be the point 
# where we first encounter either `p` or `q`.

# 3. Implementation Details:
#- Start at Root: Initialize a pointer at the root of the BST. This is where the search for the LCA begins.
#- Traversing the Tree: Use a while loop to traverse the tree. At each step, compare the values of `p` and `q` with 
# the current node's value to decide the direction:
    # - If both `p` and `q` are greater than the current node's value, move to the right child.
    # - If both are smaller, move to the left child.
    # - If they diverge (one is smaller, the other larger), or if we encounter `p` or `q`, we have found the LCA.
#- Return LCA: The node where the divergence happens (or where we first find `p` or `q`) is returned as the LCA.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        current = root
        while current:
            # If both p and q are greater than parent
            if p.val > current.val and q.val > current.val:
                current = current.right
            # If both p and q are less than parent
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                # We have found the split point, i.e. the LCA node.
                return current
        return None

# 4. Explanation
# • Start by setting the current node to the root of the BST.
# • Traverse the tree iteratively. If both p and q are less than the current node, move to the left child. If both 
# are greater, move to the right child.
# • The moment you find the first node where p and q diverge (one is on the left and the other is on the right), or 
# one of p or q matches the current node (meaning the current node is one of the ancestors), you've found the LCA.

# 5. Time & Space Complexities
# • Time Complexity: O(h), where h is the height of the tree. In the worst case, you'll travel from the root to the 
# leaf.
# • Space Complexity: O(1), as no additional space is used that depends on the size of the tree. The space used is 
# constant, just a few pointers to track the current node.
    