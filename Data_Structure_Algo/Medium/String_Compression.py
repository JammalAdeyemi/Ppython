## String Compression
# Given an array of characters chars, compress it using the following algorithm: Begin with an empty string s. 
# For each group of consecutive repeating characters in chars:
# • If the group's length is 1, append the character to s.
# • Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array 
# chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # Initialize pointers and the start index for counting
        write = start = 0
        
        # Iterate through the characters
        for read in range(len(chars)):
            # If the end of the list is reached or the current and next chars are different
            if read + 1 == len(chars) or chars[read] != chars[read + 1]:
                # Write the current char to the write pointer
                chars[write] = chars[start]
                write += 1
                # If more than one occurrence, write the count as well
                if read > start:
                    for digit in str(read - start + 1):
                        chars[write] = digit
                        write += 1
                # Update the start pointer
                start = read + 1
        
        # Return the new length after compression
        return write

## Explanation
# • Pointers: Use two pointers, read to go through the original list, and write to keep track of where to write the 
# compressed characters.
# • Iterating and Counting: Iterate through chars with the read pointer, counting the occurrences of each character 
# until a different character or the end of the list is reached.
# • Writing Characters and Counts: For each group, write the character and, if the group length is greater than one,
# write the length as individual digits.
# • In-Place Modification: The compression is done within the original list, modifying it to form the compressed 
# version.
# • Returning New Length: The write pointer indicates the length of the compressed character list.

## Time & Space Complexities
# • Time Complexity: O(n), where n is the number of characters in the list. We're processing each character once.
# • Space Complexity: O(1), as we are modifying the input list in place and not using any additional space that 
# grows with the size of the input. The extra space used is for a constant number of variables (write, start, and 
# read).
    