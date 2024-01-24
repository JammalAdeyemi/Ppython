# Maximum Depth of N-ary Tree
# Given a n-ary tree, find its maximum depth. The maximum depth is the number of nodes along the longest 
# path from the root node down to the farthest leaf node.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

## Thought Process and Concepts Utilized
# 1. Problem Understanding:
# -The objective is to find the maximum depth of an n-ary tree, where each node can have multiple children. 
# The maximum depth is defined as the longest path from the root node down to the farthest leaf node.
# -Understanding that an n-ary tree is a tree in which a node can have more than two children, the challenge
# lies in effectively traversing all possible paths from the root to each leaf to find the longest one.
# -It's important to recognize that the depth of a tree is the maximum depth among all its subtrees plus one 
# (for the root node).

## 2. Algorithm Choice:
# -Recursive Depth-First Search (DFS): This approach is chosen for its ability to explore each branch of the
# tree fully before moving to the next branch, making it suitable for finding the maximum depth. It naturally 
# fits the tree data structure where each node could have multiple paths (children) to explore.
# -Depth Calculation at Each Node: The algorithm calculates the depth of the tree rooted at each child node
# recursively. It then finds the maximum depth among all children and adds one to account for the current 
# node.
# -Handling Different Node Types: The algorithm considers different cases, such as when the tree is empty 
# (base case) and when a node is a leaf (no children), simplifying the recursive logic and ensuring correctness.

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # Base case: If the tree is empty
        if not root:
            return 0
        # If the node does not have any children, its depth is 1
        if not root.children:
            return 1
        # Recursively find the maximum depth of each subtree
        max_depth = 0
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))
        # Add 1 to account for the current node
        return max_depth + 1

## Explanation
# -Base Case: If the tree is empty (i.e., root is None), return 0 as the depth.
# -Leaf Node Case: If the node has no children, its depth is 1.
# -Recursive Depth Calculation: For each child of the current node, recursively calculate the depth of the
# subtree rooted at that child.
# -Finding Maximum Depth: The maximum depth of the current node is 1 (for the current node) plus the maximum
# depth among all its children.
# -Iterative Approach for Children: Iterate through each child and update max_depth to hold the maximum 
# depth found.

## Time & Space Complexities
# -Time Complexity: O(N), where N is the total number of nodes in the n-ary tree. Each node is visited once.
# -Space Complexity: O(H), where H is the height of the tree. This space is used in the recursion call stack. 
# In the worst case (a completely unbalanced tree), this could be O(N). In the best case (a completely balanced 
# tree), it would be O(log N).