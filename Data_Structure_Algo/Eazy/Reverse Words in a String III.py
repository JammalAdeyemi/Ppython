# Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

### Thought Process and Concepts Utilized
# 1.Problem Understanding:
# -The goal is to reverse the characters in each word of a given string `s`, which contains a sentence. 
# This task must be done while preserving the whitespace and the original order of the words.
# -The key challenge is to identify and individually reverse each word without altering the sentence's 
# overall structure.
# -A word is defined as a sequence of non-whitespace characters, and the words are separated by whitespace.

# 2.Algorithm Choice:
# -String Splitting and Rejoining: The solution involves splitting the sentence into individual words, 
# reversing each word, and then rejoining them. This approach is chosen for its simplicity and directness.
# -List Comprehension for Reversal: Utilizing Python's list comprehension and string slicing capabilities 
# to succinctly reverse each word and create a new list of reversed words.
# -Preservation of Word Order: By processing each word individually and then rejoining them in the original
# order, the sentence structure is maintained.

class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words
        words = s.split()
        # Reverse each word and store in a new list
        reversed_words = [word[::-1] for word in words]
        # Join the reversed words back into a sentence
        return " ".join(reversed_words)


### Explanation
# -Splitting the String: `s.split()` splits the string `s` into a list of words.
# -Reversing Each Word: A list comprehension is used to create a new list, where each word is reversed 
# (`word[::-1]`).
# -Rejoining Words: The list of reversed words is then joined back into a single string, with each word 
# separated by a space, using `" ".join(reversed_words)`.

### Time & Space Complexities
# -Time Complexity: O(n), where `n` is the length of the string `s`. The split, reverse, and join operations 
# all have linear time complexity relative to the length of the string or the number of words.
# -Space Complexity: O(n), as additional space is used to store the list of words and the reversed words. 
# The space used is proportional to the length of the input string.
    