# 1. Longest Even Length Word
# Consider a string, sentence, of words separated by spaces where each word is a substring consisting of English 
# alphabetic letters only. Find the first word in the sentence that has a length which is both an even number and 
# greater than or equal to the length of any other word of even length in the sentence. If there are multiple words 
# meeting the criteria, return the one which occurs first in the sentence.

def longestEvenWord(sentence):
    # Split the sentence into words
    words = sentence.split()
    longest_word = ""
    for word in words:
        # Check if the word is even and longer than the current longest word
        if len(word) % 2 == 0 and len(word) > len(longest_word):
            longest_word = word
    return longest_word if longest_word else "00" # Return "00" if no word is found

# 2. ClosetNumbers
# Given an array of distinct integers, determine the minimum absolute difference between 
# any two elements. Print all element pairs with that difference in ascending order.
def closestNumbers(numbers):
    # Sort the array in ascending order
    numbers.sort()
    min_difference = float('inf')

    # Find and store the minimum absolute difference between any two elements
    for i in range(len(numbers)-1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff < min_difference:
            min_difference = diff

    # Print all pairs that have the minimum absolute difference
    for i in range(len(numbers)-1):
        if abs(numbers[i] - numbers[i+1]) == min_difference:
            print(numbers[i], numbers[i+1])

    