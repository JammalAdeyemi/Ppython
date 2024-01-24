# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Intuition
# To solve this problem, we can use a hash table to store the complement of each number in the input array. 
# We iterate through the array and check if the current number's complement exists in the hash table. 
# If it does, we have found the two numbers that add up to the target. Otherwise, we add the current number's 
# complement to the hash table.
 
# Approach
# 1. Create a hash table to store the complement of each number in the input array.
# 2. Iterate through the input array and check if the current number's complement exists in the hash table.
# 3. If it does, return the indices of the two numbers.
# 4. Otherwise, add the current number's complement to the hash table.

# Complexity
# - Time complexity: O(n), where n is the length of the input array "nums". We iterate through the array once.
# - Space complexity: O(n), where n is the length of the input array "nums". In the worst case, we may need to store all the elements of the array in the hash table.

# Code
class Solution(object):
    def twoSum(self, nums, target):
        store = {}
        for i in range(len(nums)):
            if nums[i] in store:
                return [store[nums[i]], i]
            else:
                store[target - nums[i]] = i