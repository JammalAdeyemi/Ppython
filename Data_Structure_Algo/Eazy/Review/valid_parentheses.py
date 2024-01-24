# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

## Thought Process and Concepts Utilized
# 1. Problem Understanding:
# • The problem involves checking if a string of brackets is valid, which means every opening bracket must be closed 
# by the same type of bracket and in the correct order.
# • The string only contains characters: '(', ')', '{', '}', '[' and ']'.

# 2. Algorithm Choice:
# • Stack Data Structure: A stack is ideal for this problem because it efficiently handles the Last-In-First-Out 
# (LIFO) nature of bracket pairing.
# • Mapping Brackets: A mapping of closing to opening brackets helps in quickly checking if the bracket pairs are 
# valid.

# 3. Implementation Details:
# • Stack for Opening Brackets: Each time an opening bracket is encountered, it is pushed onto the stack.
# • Handling Closing Brackets: When a closing bracket appears, the stack is checked. If the top of the stack matches
# the corresponding opening bracket (using the bracket mapping), it's a valid pair, and the bracket is popped from 
# the stack. Otherwise, the string is invalid.
# • Complete Traversal: The string must be completely traversed to ensure all brackets are checked.

# 4.Time & Space Complexities:
# • Time Complexity: O(n), where n is the length of the string. We traverse the string once, and each operation in 
# the stack (pushing and popping) is O(1).
# • Space Complexity: O(n) in the worst case (when all characters are opening brackets, and they all get pushed onto 
# the stack). Generally, the space complexity depends on the number of opening brackets in the string.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] # Initialize a stack to keep track of opening brackets
        bracket_map = {")": "(", 
                       "}": "{", 
                       "]": "["
                    } # Dictionary to map closing brackets to their corresponding opening brackets
        for char in s: # Iterate through each character in the string
            if char in bracket_map: # If the character is a closing bracket
                # Pop the top element from the stack if it's not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element: # Check if the popped element matches the corresponding opening bracket
                    return False
            else: # If it's an opening bracket, push it onto the stack
                stack.append(char)

        return not stack # If the stack is empty, all brackets are properly closed and the string is valid

## Explanation
# 1. Stack Initialization: A stack is used to keep track of opening brackets.
# 2. Bracket Mapping: A dictionary (bracket_map) maps each closing bracket to its corresponding opening bracket.
# 3. Traversing the String: The string is traversed character by character.
# • If a closing bracket is encountered, the stack's top element (if it exists) is compared with the corresponding 
# opening bracket. If they don't match, the string is invalid.
# • If an opening bracket is encountered, it is pushed onto the stack.
# 4. Validity Check: After the entire string has been processed, the stack should be empty for the string to be valid. 
# Any remaining opening brackets in the stack imply an invalid string.      
