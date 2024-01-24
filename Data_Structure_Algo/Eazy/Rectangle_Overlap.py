# Rectangle Overlap
# An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its 
# bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel 
# to the X-axis, and its left and right edges are parallel to the Y-axis.

# Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch 
# at the corner or edges do not overlap. Given two axis-aligned rectangles rec1 and rec2, return true if they 
# overlap, otherwise return false.

### Thought Process and Concepts Utilized
# 1. Problem Understanding:
#- The task is to determine if two axis-aligned rectangles, defined by their bottom-left and top-right corners, 
# overlap.
#- Overlap means that there is a positive area of intersection, and mere touching at edges or corners doesn't count 
# as overlapping.
#- Understanding the geometry of rectangles and their relative positions is crucial to solving this problem.

# 2. Algorithm Choice:
#- Geometric Positioning Analysis: The chosen approach is to analyze the relative positioning of the rectangles. If
# one rectangle is entirely to the left, right, above, or below the other, they don’t overlap.
#- Boundary Checking: By comparing the x and y coordinates of the corners of the rectangles, we can determine if 
# such non-overlapping conditions exist.
#- Efficient and Direct: This method is straightforward and doesn't require complex calculations or additional data 
# structures.

# 3. Implementation Details:
#- Extract Coordinates: First, extract the coordinates of both rectangles for clarity and ease of use.
#- Left/Right Check: Compare the right edge of one rectangle with the left edge of the other to see if one is 
# completely to the left of the other. Repeat this for the opposite sides.
#- Top/Bottom Check: Similarly, compare the top and bottom edges. If one rectangle is completely below or above the 
# other, they do not overlap.
#- Conclusion: If none of these non-overlapping conditions are met, the rectangles must overlap, so return `True`. 
# Otherwise, return `False`.

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        Check if two rectangles overlap.
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        # Check if one rectangle is to the left of the other
        if x2 <= x3 or x4 <= x1:
            return False
        # Check if one rectangle is above the other
        if y2 <= y3 or y4 <= y1:
            return False
        return True

### Explanation
#- Non-Overlapping Conditions:
  #- If the right edge of `rec1` is to the left of the left edge of `rec2` (`x2 <= x3`) or vice versa (`x4 <= x1`), 
  # the rectangles do not overlap.
  #- If the top edge of `rec1` is below the bottom edge of `rec2` (`y2 <= y3`) or vice versa (`y4 <= y1`), the 
  # rectangles do not overlap.
#- Overlap Detection: If neither of the above conditions is met, it means that the rectangles overlap, so we return
# `True`.

### Time & Space Complexities
#- Time Complexity: O(1), as the solution involves a fixed number of comparisons, independent of any variable factors.
#- Space Complexity: O(1), since the space used is constant, only for storing the extracted coordinates and performing 
# comparisons. No extra space is used that scales with the input size.
        