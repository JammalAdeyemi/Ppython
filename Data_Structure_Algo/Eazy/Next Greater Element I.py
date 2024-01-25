# Next Greater Element I
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

### Thought Process and Concepts Utilized
## 1.Problem Understanding:
# -The objective is to find the next greater element for each element in the array `nums1` based on their 
# positions in another array `nums2`, where `nums1` is a subset of `nums2`.
# -Understanding the problem requires recognizing that for any element in `nums1`, the next greater element
# is the first element that is larger than it and appears to its right in `nums2`.
# -The problem also specifies that if no such greater element exists in `nums2`, the answer should be `-1` 
# for that element.

## 2.Algorithm Choice:
# -Stack for Finding Next Greater Elements: A stack-based approach is chosen to efficiently find the next 
# greater elements in `nums2`. The stack helps keep track of elements for which the next greater element 
# hasn't been found yet.
# -Monotonic Stack Concept: The approach uses the concept of a monotonic stack where elements are popped from
# the stack when a greater element is encountered in `nums2`. This efficiently identifies the next greater
# element for those popped items.
# -Dictionary for Mapping Results: A dictionary (`next_greater`) is used to map each element in `nums2` to 
# its next greater element. This allows for quick lookup when answering queries for elements in `nums1`.
# -Single Pass Through `nums2`: The algorithm involves iterating through `nums2` only once, and during this
# iteration, it determines the next greater element for each number in `nums2`. This single-pass approach 
# is efficient and minimizes the need for multiple scans of the array.

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Dictionary to hold the next greater element for each number in nums2
        next_greater = {}
        stack = []

        # Iterate through nums2 to find the next greater elements
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # For numbers not having a next greater element
        for num in stack:
            next_greater[num] = -1

        # Answer queries for each element in nums1
        return [next_greater[num] for num in nums1]

## Explanation
# -Stack for Tracking: Use a stack to keep track of the elements in `nums2` that we're trying to find the
# next greater element for.
# -Finding Next Greater Elements: As we iterate over `nums2`, for each number, we check if it is greater than
# the element at the top of the stack. If it is, we've found the next greater element for the stack's top
# element. We store this in the `next_greater` dictionary and pop the element from the stack.
# -Handling Remaining Elements: After the iteration, any elements left in the stack don't have a next greater
# element in `nums2`, so we assign `-1` as their next greater element in the dictionary.
# -Answering Queries for `nums1`: For each element in `nums1`, we use the `next_greater` dictionary to find
# the next greater element in `nums2`.

## Time & Space Complexities
# -Time Complexity: O(n + m), where `n` is the length of `nums1` and `m` is the length of `nums2`. The 
# iteration over `nums2` and the construction of the result for `nums1` are both linear in the size of the
# respective arrays.
# -Space Complexity: O(m), due to the extra space used by the stack and the `next_greater` dictionary, 
# where `m` is the size of `nums2`. The size of the stack and the dictionary is bounded by the number of 
# elements in `nums2`.
        

