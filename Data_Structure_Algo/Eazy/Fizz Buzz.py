# Fizz Buzz
# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

class Solution(object):
    def fizzBuzz(self, n):
        """
        Return a string array for the Fizz Buzz problem.
        :type n: int
        :rtype: List[str]
        """
        answer = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer

### Explanation
# -Iteration: The loop iterates from 1 to `n`, inclusive.
# -Divisibility Check:
    # -Divisible by 3 and 5: If `i` is divisible by both 3 and 5 (i.e., `i % 3 == 0` and `i % 5 == 0`), append "FizzBuzz" to `answer`.
    # -Divisible by 3: If `i` is only divisible by 3, append "Fizz".
    # -Divisible by 5: If `i` is only divisible by 5, append "Buzz".
    # -None of the Above: If none of these conditions are true, append the string representation of `i`.
# -Result: The `answer` list contains the Fizz Buzz representation for each number from 1 to `n`.

### Time & Space Complexities
# -Time Complexity: O(n), where `n` is the input integer. The solution requires a single pass through the numbers from 1 to `n`.
# -Space Complexity: O(n), as the space used is for storing the answer list, which contains `n` elements.