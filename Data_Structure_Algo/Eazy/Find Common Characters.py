# Find Common Characters
# Given a string array words, return an array of all characters that show up in all strings within the words(including duplicates). You may return the answer in any order.

### Thought Process and Concepts Utilized
# 1.Problem Understanding:
# -The task is to identify characters that are common to all strings in an array `words`. These common 
# characters include duplicates, and the challenge is to find them efficiently.
# -An essential aspect of the problem is understanding that a character is considered common only if it 
# appears in every string in the array, and as many times as its least frequency across these strings.
# -The problem requires a method to compare character frequencies across multiple strings and identify the 
# minimum occurrence of each character.

# 2. **Algorithm Choice**:
# -Frequency Counting with Counter: The `Counter` class from Python's `collections` module is chosen for 
# its ability to efficiently count occurrences of each character in a string. This functionality is key to 
# solving the problem as it allows for an easy comparison of character frequencies across different strings.
# -Intersection of Counters: Using the intersection operation (`&`) on Counters to find common elements. 
# This operation is ideal for this problem because it retains only those characters that are present in 
# both Counters and assigns them the minimum count seen in either. By iteratively intersecting Counters of 
# all strings, only the characters common to all strings are retained, with their counts reflecting the 
# minimum times they appear across all strings.
# -Iterative Approach: The solution starts with the character frequencies of the first word and iteratively 
# updates this with the intersection of character frequencies from subsequent words. This approach ensures 
# that only the characters common to all strings are kept in the final count.


from collections import Counter
class Solution:
    def commonChars(self, words):
        """
        Find common characters that appear in all strings within the words.
        :type words: List[str]
        :rtype: List[str]
        """
        # Initialize the common character count with the first word
        common_count = Counter(words[0])
        # Compare with the character count of each subsequent word
        for word in words[1:]:
            common_count &= Counter(word)
        # Convert the common character count back to a list of characters
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)

        return result


### Explanation
# -Initialize Common Count: Start with counting characters in the first word using `Counter` from Python's
# `collections` module.
# -Iterate Over Words: For each subsequent word, calculate its character count and perform an intersection
# (`&`) with `common_count`. This operation retains only the characters that are common between the 
# current `common_count` and the current word, with their counts being the minimum seen so far.
# -Building the Result: Iterate through the `common_count` dictionary. For each character and its count, 
# add that character to the result list `count` times.
# -Return Result: The `result` list contains all the common characters including duplicates.

### Time & Space Complexities
# -Time Complexit*: O(N * M), where `N` is the number of words in `words` and `M` is the average length of
# the words. Each word is processed to count characters, and intersections are performed.
# -Space Complexity: O(M), the space used by `common_count` and `result`, where `M` is the length of the 
# longest word. In the worst case, all characters in the longest word might be common.
    