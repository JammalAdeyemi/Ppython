# For each number in an array, get the sum of its factors. Return an array of results.
# Example
# arr = [12]
# The factors of arr[0] = 12 are [1, 2, 3, 4, 6, 12]. The sum of these factors is 28, so we return 28.
# Function Description
# Complete the function maxSubsetSum in the editor below.
# maxSubsetSum has the following parameter(s):
#     int arr[n]: an array of integers
# Returns: long[n]: the sums calculated for each arr[i]
# Constraints
# 1 ≤ n ≤ 10^3
# 1 ≤ arr[i] ≤ 10^9

def maxSubsetSum(arr):
    def get_factors(num):
        factors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.append(i)
                if i != num // i:
                    factors.append(num // i)
        return factors

    result = []
    for num in arr:
        factors = get_factors(num)
        result.append(sum(factors))

    return result

    
    