# You would like to set a password for an email account. However, there are two restrictions on the format of the password. 
# It has to contain at least one uppercase character and it cannot contain any digits. You are given a string S consisting of N 
# alphanumerical characters. You would like to find the longest substring of S that is a valid password. A substring is defined 
# as a contiguous segment of a string.
# For example, given "aBa", the substrings that are valid passwords are "B" and "Ba". Note that "aBa" is not a substring and 
# "a0B" is not a valid password.
# Write a function:
# def solution(S)
#that, given a non-empty string S consisting of N characters, returns the length of its longest substring that is a valid 
# password. If there is no such substring, your function should return -1.
# For example, given "aBa",
# ", your function should return 2, as explained
# above. Given "aobb",
# ", your function should return -1, since there is no
# substring that satisfies the restrictions on the format of a valid password.
# Assume that:
# • N is an integer within the range [1.200];
# • string S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9).
def solution(S):
    max_length = -1  # Initialize to -1, assuming there's no valid password substring
    start = 0  # Start pointer for the current substring
    has_uppercase = False  # Flag to check if the current substring contains an uppercase character

    for end in range(len(S)):
        if S[end].isupper():
            has_uppercase = True  # Mark that the current substring contains an uppercase character

        if S[end].isdigit():
            start = end + 1  # If a digit is encountered, reset the start pointer

        # Calculate the length of the current substring
        current_length = end - start + 1

        # Check if the current substring is valid
        if has_uppercase and current_length > max_length:
            max_length = current_length

    return max_length

# Write a function solution that returns an arbitrary integer which is greater than N, not greater than 100, and that ends 
# with 0. You can assume that N is between 1 and 999,999,999. For example, given N = 27, your function may return 60 and 
# for N = 30,your function may return 40.
def solution(N):
    # Check if last digit is 0
    if N % 10 == 0:
        # If so, add 10 to make next number
        return N + 10
    else:
        # If not, divide by 10 and add 1 to make next number. Then multiply by 10 to get the next multiple of 10
        return ((N // 10) + 1) * 10

# There is a string S made of words "one" and "two" separated by single "+" and "-" signs. The string represents a valid 
# sequence of additions and subtractions of the digits 1 and 2. 
# Calculate the result of the expression represented by S. Write a function:
#               def solution (S)
# that, given a string S, returns the result of the mathematical expression it represents.
# Examples:
# 1. Given S = "one+two-one-one+two+one", the string represents the expression 1 + 2 - 1 - 1 + 2 + 1. Its result is equal to 4. 
# The function should return 4.
# 2. Given S = "two-two-one-two", the function should return -3.
# 3. Given S = "two", the function should return 2.
# Assume that:
# • the length of string S is within the range [3.499);
# • string S is made only of words "one" and "two" separated by single "+" or "-" signs;
# • string S begins and ends with a word.
def solution(S):
    # Replace 'one' with '1'
    S = S.replace("one", "1")
    # Replace 'two' with '2'
    S = S.replace('two', "2")
    # Evaluate the expression
    res = eval(S)
    return res

#Initially, string S of length N is given. Then N-1 operations are applied to it: move the first letter of S to the end. 
# How many times is the first letter of S the same as the last letter? For example, given S = "abbaa", the obtained 
# sequence of strings is:
# abbaa → bbaaa →› baaab → aaabb -› aabba
# Three of them have the same first and last letter.
# Write a function:
#       def solution (S)
# that, given a string S of length N, consisting of letters 'a' and/or 'b', returns the number of times the first letter is the same as the last in the obtained sequence of strings.
# Examples:
# 1. Given S = "abbaa", the function should return 3, as described above.
# 2. Given S = "aaaa", the function should return 4. The first and last letters are always the same.
# 3. Given S = "abab", the function should return 0. The first and last letters are always different.
# Write an efficient algorithm for the following assumptions:
# • N is an integer within the range [2.200,000];
# • string S is made only of the characters 'a' and/or 'b.
def solution(S):
    # Initialize a count variable to keep track of the number of times the first and last characters are equal
    count = 0
    
    # Get the length of the input string
    n = len(S)
 
    # Iterate over each character in the string
    for each in range(n):
        # Check if the first and last characters of the string are equal
        if S[0] == S[-1]:
            # If they are equal, increment the count variable
            count += 1
        
        # Rotate the string by moving the first character to the end
        S = S[1:] + S[0]
    # Return the final count value
    return count

# Your task is to provide a suite of tests for an invert function, using Pytest framework, covering all the requirements below.
# Description of the invert function invert function accepts a string and returns a string.
# • When the string is empty it returns empty string.
# • When the argument passed to the method is None it returns an empty string
# • When the string has exactly one character the same string is returned
# • When the string is longer then 1 character its inverted version is returned.

# Examples of invert function usage
# from inverter import invert 
# invert("a"); // returns "a" 
# invert (None); // returns "" 
# invert ("abcd"); // return "dcba"

# Requirements
# • Your task is to implement a suite of tests in Pytest that will test all the possible behaviours of the invert function, as described above.
# • Your suite of tests will be run against multiple (wrong and correct) implementations of invert function.
# • All tests must pass for correct implementation. Otherwise you will receive 0%, so make sure that all tests pass for the correct one before submitting the task.
# • For a wrong implementation of the invert function, at least one of the test cases should fail.
# • Tests should be written using Python 3.8 and Pytest 5.3.5.
from inverter import invert
def test_invert_empty_string():
    assert invert("") == ""

def test_invert_none_input():
    assert invert(None) == ""

def test_invert_single_character():
    assert invert("a") == "a"
    assert invert("z") == "z"

def test_invert_long_string():
    assert invert("abcd") == "dcba"
    assert invert("hello") == "olleh"
    assert invert("python") == "nohtyp"

# The objective of this task is to write an API with one GET endpoint.
# Requirements
# You are required to write an API with Python and the Flask library that will contain the following endpoint:
# • GET /users
# • endpoint should return the status code 200 on a successful request;
# • endpoint should return the data taken from the mocked-up database using the provided helper function get_users. 
# This function returns a list of dictionaries containing id (number), name (string) and role (string). An example list might 
# appear as follows:
# [{
# "id" :1,
# "name" :"John",
# "role": "admin"
# },
# {
# "id": 2,
# "name": "Juan"
# "role": "developer"
# }
# ]
# • endpoint should accept a query parameter name which will corain a string;
# • when parameter name is provided, all users whose name property is equal to the name query parameter must be returned 
# (there may be more than one match). If no users with the given name are found, an empty list must be returned.

# Hints
# • Your solution will be evaluated based on its correctness; performance and coding style will not be assessed.
# • You can assume that the id, name and role properties of the users returned from the database are all present and of the 
# correct types. You do not have to verify them.
# • You do not have to take care of unsuccessful requests; the response is always successful and the status code must equal 200.

# Initial code
# The initial code contains imports from the Flask library and the get_users method impprt. Your task is to implement the 
# GET /users endpoint. Do not modify the main method.

# Examples
# Given a database helper method returning the following data:
# [{
# "id": 1,
# "name": "John",
# "role": "admin"
# },
# {
# "id": 2,
# "name": "Juan",
# "role": "developer"
# }
# ]
# • A request to GET /users should return 200 and the following payload:
# [{
# "id": 1,
# "name": "John",
# "role": "admin"
# },
# {
# "id": 2,
# "name": "Juan"
# "role": "developer"
# }
# ]
# • A request to GET /users?name=John should return 200 and the following payload:
# [
# {
# "id": 1,
# "name":
# "John"
# "role": "admin"
# }
# ]
# • A request to GET /users?name=Jane should return 200 and the following payload:
# []
from flask import Flask, jsonify, request
from db_users import get_users

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users_endpoint():
    name = request.args.get('name')
    users = get_users()

    if name:
        filtered_users = [user for user in users if user['name'] == name]
        return jsonify(filtered_users), 200
    else:
        return jsonify(users), 200

if __name__ == '__main__':
    app.run()