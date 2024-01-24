## Maximum Product of Three Numbers
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

## Thought Process and Concepts Utilized
# 1. Problem Understanding:
# The objective is to find the maximum possible product of three numbers from a given integer array.
# The array can contain both positive and negative numbers, impacting the product calculation.
# The challenge lies in determining the combination of three numbers that yields the highest product, considering negative numbers can turn a product larger when paired.

# 2. Algorithm Choice:
# Sorting: Sorting the array simplifies the identification of the necessary elements (the largest and the smallest) to consider for the maximum product.
# Comparing Products: After sorting, the potential maximum products come from either the three largest numbers or a combination of the two smallest (potentially negative) and the largest number.

# 3. Implementation Details:
# Sort the Array: The array is sorted to arrange numbers in ascending order, allowing easy access to both the smallest and largest values.
# Calculate Two Products:
    # - The product of the three largest numbers (`nums[-1] * nums[-2] * nums[-3]`).
    # - The product of the two smallest numbers and the largest number (`nums[0] * nums[1] * nums[-1]`), considering the impact of negative numbers.
# Determine Maximum Product: The maximum of these two products is the result, as it covers all possible combinations leading to the maximum product.

# 4. Time & Space Complexities:
# Time Complexity: O(n log n), where `n` is the number of elements in the array. This complexity arises from sorting the array, which is the most time-consuming part of the algorithm.
# Space Complexity: O(1), assuming an in-place sorting algorithm is used. The space complexity is constant as no additional space that scales with the size of the input is required; only a fixed number of variables are used.

class Solution(object):
    def maximumProduct(self, nums):
        """
        Find the maximum product of three numbers in the array.
        :type nums: List[int]
        :rtype: int
        """
        # Sort the array
        nums.sort()

        # The product of the three largest numbers
        max_product = nums[-1] * nums[-2] * nums[-3]

        # The product of the two smallest numbers and the largest number
        max_product_with_negatives = nums[0] * nums[1] * nums[-1]

        # Return the maximum of the two products
        return max(max_product, max_product_with_negatives)