## Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or 
# phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters 
# exactly once.

# 1. Problem Understanding:
# - An anagram is a word formed by rearranging the letters of another, using all original letters exactly once.
# - The task is to check if string t is an anagram of string s.

# 2. Algorithm Choice:
# • Counting Characters: The approach is to count the occurrences of each character in both strings and compare these counts.
# • Set to Avoid Repetition: By converting s to a set, each character is considered only once, avoiding redundant comparisons.

# 3. Implementation Details:
# •Length Check: The code first checks if s and t are of different lengths. If so, they cannot be anagrams, and it returns False.
# • Character Count Comparison: It iterates through each unique character in s (using set(s)) and compares the count of that character in both s and t using the count method. If there's a mismatch, it returns False.
# • Return True: If no mismatches are found, it concludes that t is an anagram of s and returns True.

# 4. Time & Space Complexities:
# • Time Complexity: O(n²), where n is the length of string s. This is because s.count(idx) and t.count(idx) are both O(n) operations, and they are called for each unique character in s. In the worst case (when all characters in s are unique), this results in n O(n) operations.
# • Space Complexity: O(n), mainly due to the creation of a set from string s. The space used by the set depends on the number of unique characters in s.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Check if the lengths of the two strings are different
        if len(s) != len(t):
            return False
        # Iterate through the unique characters in string s    
        for idx in set(s):
            # Compare s.count(l) and t.count(l) for every index i from 0 to 26.
            if s.count(idx) != t.count(idx):
                return False
        # If all character counts match, return True
        return True    

# # Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# # If the inputs contain Unicode characters, the solution can still be applied with minor adaptations. Unicode characters can be treated similarly to ASCII characters in this context, as the fundamental principle of counting character occurrences remains the same. However, a few considerations should be kept in mind:
# # 1. Unicode Characters Set: Unicode characters include a much wider range of symbols than ASCII. This includes characters from various languages, emojis, and other symbols. Thus, the set of characters to be considered is larger.
# # 2. Using a Hash Map (Dictionary) for Counting:
# # • For Unicode characters, it is efficient to use a hash map (like a Python dictionary) for counting character occurrences. This is because the set and count approach may become inefficient due to the potentially large range of different characters.
# # • The dictionary will map each character to its frequency in the string.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Check if the lengths of the two strings are different
        if len(s) != len(t):
            return False

        # Use dictionaries to count occurrences of each character in both strings
        count_s, count_t = {}, {}
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # Compare the two dictionaries
        return count_s == count_t

# # Adaptation for Unicode Characters
# # • Counting with Dictionaries: The code uses dictionaries to count the occurrences of each character, which is efficient for Unicode characters.
# # • Flexibility for Larger Character Set: This approach is robust regardless of the character set size, accommodating the extensive range of Unicode characters.

# # Time & Space Complexities
# # • Time Complexity: O(n + m), where n is the length of string s, and m is the length of string t. Each string is traversed once.
# # • Space Complexity: O(n + m), as the space is required for the dictionaries storing the character counts. The space complexity depends on the number of unique characters in the strings.
        