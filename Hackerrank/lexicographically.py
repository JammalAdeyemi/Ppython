# Given two strings s and t, both consisting of lowercase English letters and digits, your task is to calculate how many ways 
# exactly one digit could be removed from one of the strings so that s is lexicographically smaller than t after the removal. 
# Note that we are removing only a single instance of a single digit, rather than all instances 
# (eg: removing 1 from the string a11b1c could result in a1b1c or a11bc, but not abc).

def solution(s, t):
    count = 0
    # Iterate over each character in string s
    for i in range(len(s)):
        # Check if the current character is a digit
        if s[i].isdigit():
            # If it is, remove it from string s and store the result in a new variable called new_s
            new_s = s[:i] + s[i+1:]
            # Check if new_s is lexicographically smaller than t
            if new_s < t:
                count += 1
    # Iterate over each character in string t
    for i in range(len(t)):
        # Check if the current character is a digit
        if t[i].isdigit():
            # If it is, remove it from string t and store the result in a new variable called new_t
            new_t = t[:i] + t[i+1:]
            # Check if s is lexicographically smaller than new_t
            if s < new_t:
                count += 1

    return count



