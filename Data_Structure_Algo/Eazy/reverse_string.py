## Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s. 
# You must do this by modifying the input array in-place with O(1) extra memory.

# Thank you for this interesting problem. When I think about reversing a string, the first thing that comes to mind is how we can achieve this in the 
# most space-efficient way. Since we're asked to do this in-place, with O(1) extra memory, it immediately directs me towards a two-pointer approach.

# The beauty of this approach lies in its simplicity and elegance. We can place one pointer at the start and another at the end of the string. 
# These pointers essentially act as markers, allowing us to swap the characters at these positions. As we continue swapping, 
# we move the pointers closer to the center. The left pointer moves right, and the right pointer moves left. The process continues until the pointers 
# meet or cross each other, which signals that the entire string has been reversed.

# This method is wonderfully efficient because it doesn't require any additional space for another string or array; the reversal happens within the 
# original array. It's like a dance where two partners (the pointers) gracefully swap positions, moving towards and away from each other, 
# until the dance (the string) is mirrored into its reverse form.

# Moreover, this approach is not just space-efficient but also time-efficient. It has a linear time complexity, O(n), where n is the length of the 
# string. Every element is visited once, making it as efficient as it can be given the constraints.

class Solution(object):
    def reverseString(self, s):
        """
        Reverses a string in place.
        The function takes a list of characters as input and reverses the characters within the same list. 
        This is achieved by using a two-pointer approach, which ensures that the space complexity remains O(1), as no additional storage is created.

        :type s: List[str]: The string to be reversed, represented as a list of characters.
        :rtype: None: The function doesn't return anything since it modifies the list in place.
        """
        # Initialize two pointers, one at the beginning (left) and one at the end (right) of the string.
        left = 0
        right = len(s) - 1

        # Loop until the two pointers meet in the middle.
        while left < right:
            # Swap the characters at the left and right pointers.
            s[left], s[right] = s[right], s[left]
            # Move the left pointer one step forward and the right pointer one step backward.
            left += 1
            right -= 1
