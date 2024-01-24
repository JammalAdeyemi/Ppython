# Remove All Adjacent Duplicates In String
# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two 
# adjacent and equal letters and removing them. We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

### Thought Process and Concepts Utilized
# 1. Problem Understanding:
#- The task is to repeatedly remove adjacent duplicate characters from a given string until no more such pairs exist.
#- The challenge lies in efficiently identifying and removing these adjacent duplicates, bearing in mind that the 
# removal of one pair might create a new pair.
#- The process is iterative and needs to be repeated until no further removals are possible.

#2. Algorithm Choice:
#- Stack-Based Approach: A stack is chosen for its Last-In-First-Out (LIFO) property, which is ideal for keeping 
# track of characters and identifying adjacent duplicates.
#- Iterative Removal: The stack allows for efficient removal of duplicates as soon as they are detected. When a 
# character is the same as the top of the stack, it signifies an adjacent duplicate pair, which can then be removed 
# instantly.
#- Linear Pass: This approach requires only a single pass through the string, making it efficient in terms of time 
# complexity.

#3. Implementation Details:
#- Stack Initialization: Start with an empty stack to store characters from the string.
#- Traversing the String: Iterate through each character in the string.
    #- Duplicate Detection and Removal: If the current character is the same as the top of the stack, pop the top of
    # the stack (removing both characters of the duplicate pair).
    #- Adding Non-Duplicates: If the stack is empty or the top element is different from the current character, push
    # the current character onto the stack.
#- Reconstructing the Result: After processing all characters, the stack contains the string with duplicates removed. 
# Convert the stack back to a string to get the final result.

class Solution(object):
    def removeDuplicates(self, s):
        """
        Remove all adjacent duplicates from the string s.
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)

### Explanation
#- Using a Stack: Initialize an empty stack to keep track of the characters.
#- Iterating Through the String: For each character in the string `s`:
  #- Duplicate Check: If the stack is not empty and the top element of the stack is the same as the current 
  # character, pop the top element from the stack (removing the adjacent duplicates).
  #- Non-Duplicate: If the stack is empty or the top element is different, push the current character onto the stack.
#- Reconstructing the Result: After the iteration, the stack contains the final string with all adjacent duplicates
# removed. Convert the stack back to a string and return it.

### Time & Space Complexities
#- Time Complexity: O(n), where `n` is the length of the string `s`. Each character in the string is processed once.
#- Space Complexity: O(n) in the worst case, where all characters are distinct and pushed onto the stack. In the best case, 
# where the string is made of all duplicates, the space complexity would be O(1).
        