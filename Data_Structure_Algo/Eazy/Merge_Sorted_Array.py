## Merge Sorted Array
# You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in `nums1` and `nums2` respectively. Merge `nums1` and `nums2` into a single array 
# sorted in non-decreasing order. The final sorted array should not be returned by the function, but instead be 
# stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements 
# denote the elements that should be merged, and the last `n` elements are set to 0 and should be ignored. `nums2` has a
# length of n.

### Thought Process and Concepts Utilized
# 1. Problem Understanding:
# - The task requires merging two sorted arrays, `nums1` and `nums2`, into one sorted array, which should be stored 
# in `nums1`.
# - The size of `nums1` is large enough to hold the combined elements of both arrays, with `m` initial elements 
# followed by `n` zeros where the elements of `nums2` will fit.
# - It's important to merge the arrays in a way that doesn't overwrite the elements of `nums1` that haven't been 
# merged yet.

# 2. Algorithm Choice:
# - Reverse Merging: Opting to fill `nums1` starting from the end, where there are placeholder zeros, ensures that 
# we do not overwrite any elements from `nums1` that are yet to be merged.
# - Three-Pointer Technique: Using three pointers—two to track the current elements to compare in `nums1` and `nums2`, 
# and one to track the position in `nums1` where the next greatest element should go—facilitates an efficient 
# in-place merge.
# - Direct Copy for Remaining Elements: If elements of `nums2` remain after `nums1` is exhausted, they can be copied
# directly to the beginning of `nums1`, as they are already sorted.

# 3. Implementation Details:
# - Initialization: Set pointers at the last element of each array (`p1` for `nums1` and `p2` for `nums2`) and a 
# pointer `p` at the end of the total length of the merged array.
# - Iterative Comparison and Merging: Iteratively compare the elements pointed by `p1` and `p2`, placing the larger 
# value in the position pointed by `p` in `nums1` and move the involved pointers backwards.
# - Finalizing Merge: After finishing the main loop, check if there are leftover elements in `nums2` (meaning `p2` 
# is not yet at `-1`) and copy them to the beginning of `nums1`, since `p1` would have already reached the start of
# the array, and `nums1` elements are already sorted.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Merge two sorted arrays nums1 and nums2 into a single sorted array in-place.
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Set pointers for nums1 and nums2 respectively
        p1, p2 = m - 1, n - 1
        
        # Set pointer for the end of the merged array
        p = m + n - 1
        
        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them
        nums1[:p2 + 1] = nums2[:p2 + 1]

## Time & Space Complexities
# • Time Complexity: O(m + n), where m and n are the lengths of the arrays to be merged. Each element from both 
# arrays is processed once.
# • Space Complexity: O(1), as the merge is done in place without using any additional storage. The space complexity
# is constant regardless of the size of the input arrays.
        