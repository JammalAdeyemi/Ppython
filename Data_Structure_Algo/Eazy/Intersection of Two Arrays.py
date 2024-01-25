# Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

### Thought Process and Concepts Utilized
## 1.Problem Understanding:
# -The task is to find the intersection of two integer arrays `nums1` and `nums2`, ensuring that each element 
# in the result is unique and can be returned in any order.
# -The key aspect of the problem is understanding what constitutes an intersection in the context of arrays
# — specifically, the elements that are common to both arrays.
# -Another important consideration is the requirement for the elements in the result to be unique, which 
# indicates the need to eliminate duplicates from the considered elements in both arrays.

## 2.Algorithm Choice:
# -Set-Based Approach: The choice to use sets is driven by two factors: sets inherently eliminate duplicates
# and they allow for efficient computation of intersections.
# -Conversion of Arrays to Sets: This step is crucial as it addresses two requirements of the problem 
# simultaneously — removing duplicates and preparing for an efficient intersection operation.
# -Intersection Operation on Sets: Utilizing the built-in set operation for intersection in Python. This 
# operation is highly optimized and directly yields the common elements between the two sets, which correspond
# to the intersection of the original arrays.
# -Returning Result as a List: Since the final result needs to be an array (list in Python), the resulting
# set is converted back to a list. This conversion is a straightforward process and aligns with the 
# problem's requirement to return the result in any order. 

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        Return the intersection of two arrays as a unique element list.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Convert both lists to sets
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        # Find the intersection of the two sets
        return list(set_nums1.intersection(set_nums2))

## Explanation
# -Convert to Sets: Convert `nums1` and `nums2` to sets, `set_nums1` and `set_nums2`. This removes duplicates
# and allows for efficient intersection operations.
# -Find Intersection: Use the `intersection` method of sets to find common elements between `set_nums1` 
# and `set_nums2`.
# -Return as List: Convert the resulting set back to a list since the problem statement asks for the result
# in the form of an array.

## Time & Space Complexities
# -Time Complexity: O(n + m), where `n` is the length of `nums1` and `m` is the length of `nums2`. The majority
# of the time is spent on converting the arrays to sets and the intersection operation.
# -Space Complexity: O(n + m) in the worst case, for the space used by the two sets. In the best case, if 
# there are many duplicates, the space complexity can be less.
        