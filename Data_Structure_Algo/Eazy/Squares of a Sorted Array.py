# Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted 
# in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # Solution with 2 Pointers
        # Time Complexity: O(n)  Space Complexity: O(n)
        """
        1. Initialize two pointers: lowValue = 0; highValue = len(nums) - 1
        2. Create a list with same length as nums to  store squared values arranged in non decreasing order
        3. Loop through the nums array "Backwards" (last index to 0) 
        
            For each i, compare the absolute values of given list at the lowValue and highValue indexes
            
            3a. If absolute value of element at index lowValue >= absolute value of element at index highValue:
                
                - Element of index i of new list = square (element at index lowValue)
                - lowValue += l (Increment lowValue)
                
            3b. Else if absolute value of element at index lowValue < absolute value of element at index highValue:
                
                - Element of index i of new list = square (element at index highValue)
                - highValue -= l (Decrement highValue)  
        """         
        # Step 1.
        lowValue = 0
        highValue = len(nums) - 1
        
        # Step 2.
        nums_square = [None] * int(len(nums))
        
        # Step 3.
        for i in range(len(nums) - 1, -1, -1):
            # Step 3a.
            if abs(nums[lowValue]) >= abs(nums[highValue]):
                nums_square[i] = nums[lowValue] * nums[lowValue]
                lowValue+=1
            # Step 3b
            else:
                nums_square[i] = nums[highValue] * nums[highValue]
                highValue-=1        
        return nums_square

# Time & Space Complexities
#- Time Complexity: O(n), where n is the number of elements in the array. The algorithm efficiently processes each
# element once.
#- Space Complexity: O(n) for the nums_square array. This space is necessary for the output and is proportional to 
# the size of the input array.