# Subarry Sum - A subarray is any contiguous block of an array element. Given an array of integers, find the 
# sum of all elements of all subarrays of that array.

def subarraySum(arr):
    # Write your code here
    sum = 0
    n = len(arr)
    for x in range(n):
        y = (n - x) * (x + 1)
        sum += arr[x] * y
    return sum



# A salesperson must sell n items in a bag with random IDs. The salesperson can remove as many as m items from the 
# bag. Determine the minimum number of different IDs the final bag can contain after performing, at most, m deletions.
# Example
# n = 6
# ids = [1, 1, 1, 2, 3, 2]
# m = 2
# Two possible actions that give the minimum 2 different IDs:
# 1. Remove 2 items with ID = 2 and the final bag wil contain item ids' = [1, 1, 1, 3]
# 2. Remove 1 item with ID = 2 and 1 item with ID=3 and the final bag will contain item ids' = [1, 1, 1, 2]
# The minimum number of distinct IDs is 2.

from collections import Counter
def deleteProducts(ids, m):
    # count the frequency of each item id
    freq = Counter(ids)
    # create a list where index i is the count of item ids that appear i times
    buckets = [0] * (len(ids) + 1)

    for id, frequency in freq.items():
        buckets[frequency] += 1
    distinct_ids = len(freq)

    for i in range(len(buckets)):
        # if the smallest frequency can be completely removed
        if m >= i * buckets[i]:
            # decrease m by the total deletions
            m -= i * buckets[i]
            # decrease the number of distinct ids by the number of ids with that frequency
            distinct_ids -= buckets[i]
        else:
            # decrease the number of distinct ids by maximum possible deletions 
            distinct_ids -= m // i
            break

    return distinct_ids

# 1. Maximum Index
# There is an infinite array of integers numbered consecutively from 0. At each step, a pointer can move from index ito index i + j, or remain where it is. The value of i begins at 0. The value of j begins at 1 and at each step, jincrements by 1. There is one known index that must be avoided. Determine the highest index that can be reached in a given number of steps.
# Example steps = 4, badElement = 6
# The pointer is limited to 4 steps and should avoid the bad item 6.

# Scenario 1: In the first step, j starts at 1. Move 1 unit to index 0 + 1 = 1 and j = 2.
# 。 At step 2, move 2 units to index 1 + 2 = 3, and j = 3.
# 。 At step 3, do not move. Otherwise, the pointer will move 3 units to the bad item 6. Now j = 4.
# 。 At step 4, move 4 units to item 3 + 4 = 7.

# Scenario 2: At step 1, remain at index 0. Now j = 2.
# 。 At step 2, move 2 units to index 0+2= 2 and j = 3.
# 。 At step 3, move 3 units to index 2+3= 5 and j = 4.
# 。 At step 4, move 4 units to index 5 + 4 = 9.

# The maximum index that can be reached is 9.
def maxStep(steps, badElement):
  # Initialize the current index to 0.
  current_index = 0
  # Initialize the maximum index that can be reached to -1.
  max_index = -1
  # Iterate over the number of steps.
  for i in range(steps):
    # Increment the current index by the current value of j.
    current_index += i + 1
    # If the current index is greater than the maximum index, update the maximum index.
    if current_index > max_index:
      max_index = current_index
    # If the current index is equal to the bad element, break out of the loop.
    if current_index == badElement:
      break
  # Return the maximum index that can be reached.
  return max_index



