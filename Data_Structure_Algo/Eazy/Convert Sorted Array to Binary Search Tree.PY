# Convert Sorted Array to Binary Search Tree
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left 
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        mid = len(nums) // 2  # Find the middle element
        # Create a TreeNode with the middle element as root
        root = TreeNode(nums[mid])
        # Recursively build the left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root

## Explanation
# -Base Case: If the array is empty (nums is None or has length 0), return None because there are no nodes
# to construct a BST.
# -Find Middle Element: The middle index is found by dividing the length of the array by 2 using integer 
# division.
# -Construct Root Node: A new TreeNode is created with the value of the middle element of the array.
# -Recursive Construction: The array is split into two subarrays - elements before the middle (left subtree)
# and elements after the middle (right subtree). The method is called recursively on these subarrays to 
# construct the left and right subtrees, respectively.
# -Return Root: The root of the newly constructed BST is returned.

## Time & Space Complexities
# -Time Complexity: O(n), where n is the number of elements in the array. Each element is visited once to 
# create a node in the BST.
# -Space Complexity: O(log n), where n is the number of elements in the array. This is the space used by 
# the recursion stack. In a balanced BST, the height (and therefore the maximum depth of the recursion 
# stack) is logarithmic relative to the number of nodes.       