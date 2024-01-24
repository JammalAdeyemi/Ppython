# Cousins in Binary Tree
# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

### Thought Process and Concepts Utilized
## 1.Problem Understanding:
# -The challenge is to determine whether two given nodes, identified by their values `x` and `y`, are cousins 
# in a binary tree. Cousins are defined as nodes that are at the same depth but have different parents.
# -A crucial aspect of the problem is understanding the tree's structure, particularly how node depths and 
# parent-child relationships are defined.
# -The problem also requires differentiating between siblings (nodes with the same parent) and cousins, which
# necessitates checking both the depth and the parent of each node.

## 2.Algorithm Choice:
# -Depth-First Search (DFS) for Depth and Parent Tracking: The choice of a DFS approach is based on its 
# effectiveness in traversing tree structures and gathering information about each node. In this case, 
# it's used to track two specific pieces of information for each node: its depth (distance from the root)
# and its parent node.
# -Recursive Helper Function: Implementing a recursive helper function, `findDepthAndParent`, simplifies the
# process of finding the depth and parent of the target nodes. The recursive nature of DFS aligns well with
# the tree's structure, allowing for an intuitive traversal process.
# -Independent Depth and Parent Calculation: The solution involves independently determining the depth and
# parent of `x` and `y`. This independent analysis is crucial, as it allows for the direct comparison of 
# the depths and parents of the two nodes, which is necessary to ascertain if they are cousins.
# -Cousin Condition Evaluation: After obtaining the depth and parent information for both nodes, the solution
# applies the cousin definition: nodes `x` and `y` are cousins if they have the same depth but different parents.
# This involves a straightforward comparison of the obtained values.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isCousins(self, root, x, y):
        """
        Determine if two nodes are cousins in a binary tree.
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        # Helper function to find the depth and parent of a given value
        def findDepthAndParent(node, val, depth, parent):
            if not node:
                return (None, None)
            if node.val == val:
                return (depth, parent)
            left = findDepthAndParent(node.left, val, depth + 1, node)
            right = findDepthAndParent(node.right, val, depth + 1, node)
            return left if left[0] is not None else right

        x_depth, x_parent = findDepthAndParent(root, x, 0, None)
        y_depth, y_parent = findDepthAndParent(root, y, 0, None)

        # Nodes are cousins if they have the same depth but different parents
        return x_depth == y_depth and x_parent != y_parent

## Explanation
# -Depth and Parent Finding: The helper function `findDepthAndParent` is a recursive function that traverses
# the tree to find the depth and parent of a given value. It returns a tuple `(depth, parent)` for the given
# value.
# -Applying the Helper Function: Apply `findDepthAndParent` separately for `x` and `y` to find their depths
# and parents.
# -Checking Cousin Condition: Two nodes are cousins if they are at the same depth (`x_depth == y_depth`) but
# have different parents (`x_parent != y_parent`).

## Time & Space Complexities
# -Time Complexity: O(n), where `n` is the number of nodes in the tree. In the worst case, the helper function
# might have to visit every node to find the depths and parents of `x` and `y`.
# -Space Complexity: O(h), where `h` is the height of the tree. This space is used by the recursion stack. 
# For a balanced tree, this would be O(log n), and for a completely unbalanced tree, it would be O(n).
    
        

