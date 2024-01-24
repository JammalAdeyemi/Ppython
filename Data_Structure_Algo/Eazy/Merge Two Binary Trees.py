# Merge Two Binary Trees
# You are given two binary trees root1 and root2. Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
# Return the merged tree.
# Note: The merging process must start from the root nodes of both trees.

# 1. Problem Understanding:
#- The task is to merge two binary trees into a single tree, adhering to the rule that overlapping nodes' values are
# summed, and non-overlapping nodes are retained as they are.
#- The problem requires an understanding of tree data structures and the ability to navigate and manipulate them.
#- A key aspect of the problem is handling various cases: when both nodes exist, when only one exists, and when 
# neither exists.

# 2. Algorithm Choice:
#– Recursive Approach: You correctly identified that recursion is an ideal choice for this problem. It allows for 
# straightforward depth-first traversal of both trees simultaneously and efficiently merges their nodes.
#- Helper Function (constructTree): The use of a helper function within mergeTrees simplifies the recursive process. 
# This encapsulation makes the code more organized and easier to follow.
#- Handling Different Cases: Your recursive function is designed to handle the key scenarios - both nodes exist, 
# only one node exists, and neither exists, ensuring a comprehensive solution that accounts for all possibilities in
# the tree structure.

# 3. Implementation Details:
#- Base Cases: You correctly implemented the base cases, returning None if both nodes are absent, root1 if root2 is 
# absent, and vice versa. These cases ensure that the merged tree retains all existing nodes from both trees.
#- Node Merging: In cases where both nodes exist, you create a new TreeNode with its value as the sum of root1 and 
# root2 nodes' values. This aligns with the merging rule specified in the problem.
#- Recursive Calls for Children: You then recursively call constructTree for both the left and right children of the
# current nodes, effectively applying the same merging logic throughout the tree.
#- Returning the Merged Tree: The helper function returns the head of the newly constructed merged tree, which is 
# then returned by the mergeTrees method.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        def constructTree(root1, root2):
            if not root1 and not root2:
                return None
            if not root2:
                return root1
            if not root1:
                return root2
            head = TreeNode(root1.val + root2.val)
            head.left = constructTree(root1.left, root2.left)
            head.right = constructTree(root1.right, root2.right)
        
            return head
        
        return constructTree(root1, root2)

# Time & Space Complexities
#- Time Complexity: O(min(m, n)), where m and n are the number of nodes in each of the two trees. The function visits
# each node at most once in both trees, but stops early if one tree is smaller.
#- Space Complexity: O(min(m, n)) in the worst case, which is the space required for the recursion stack. The 
# worst-case space complexity occurs when the trees are completely unbalanced.