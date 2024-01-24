# A format for expressing an ordered list of integers is to use a comma separated list of either

# 1. individual integers
# 2. or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
# The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans 
# at least 3 numbers. For example "12,13,15-17".
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the 
# range format.

# Example:

# range_compact([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-6,-3-1,3-5,7-11,14,15,17-20"


from typing import List

def range_compact(nums: List[int]) -> str:
  if not nums:
    return ""
  res = []
  start = nums[0]
  end = nums[0]
  for i in range(1, len(nums)):
    if nums[i] - nums[i-1] == 1:
      end = nums[i]
    else:
      if end > start:
        if end - start >=2:
          res.append(str(start) + "-" + str(end))
        else:
          res.append(str(start))
          res.append(str(end))
      else:
        res.append(str(start))
      start = nums[i]
      end = nums[i]
  if end > start:
    if end - start >=2:
      res.append(str(start) + "-" + str(end))
    else:
      res.append(str(start))
      res.append(str(end))
  else:
    res.append(str(start))
 
  return ",".join(res)
