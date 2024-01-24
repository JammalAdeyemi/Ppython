# You are given an array of integers a and an integer k. Your task is to calculate the number of ways to pick two different 
# indices i < j, such that a[i] + a[j] is divisible by k.

def solution(a, k):
    count = 0
    # Iterate over each pair of indices i and j in the array a
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            # Check if the sum of a[i] and a[j] is divisible by k
            if (a[i] + a[j]) % k == 0:
                count += 1
    return count

len(845)