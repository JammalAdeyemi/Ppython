# Moving Average from Data Stream
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
# Implement the MovingAverage class:
# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.

### Thought Process and Concepts Utilized
## 1.Problem Understanding:
# - The challenge is to maintain a running average of the most recent `size` numbers from a stream of integers.
# The key is to efficiently update the average as new numbers arrive, ensuring that only the last `size` 
# numbers are considered.
# - A moving average requires that when a new value is added to the dataset, the oldest value (if we've reached
# the window size) is removed from the consideration set for the average calculation.

## 2.Algorithm Choice:
# -Queue Data Structure: A queue (`collections.deque` in Python) is an ideal choice because it efficiently
# allows insertion at one end and removal from the other, matching the requirements of the moving average 
# calculation.
# -Maintaining Current Sum: To avoid summing all the elements of the queue every time a new value is added 
# (which would be inefficient), the current sum of all elements within the window is maintained and updated
# incrementally.
# -Window Size Enforcement: The algorithm ensures the window size is enforced by removing the oldest element
# whenever the window exceeds the specified size.

from collections import deque
class MovingAverage:
    
        def __init__(self, size: int):
            """
            Initialize your data structure here.
            """
            self.queue = deque()  # A double-ended queue to store the window's values
            self.size = size      # The size of the window
            self.current_sum = 0  # Current sum of the window's values
    
        def next(self, val: int) -> float:
            if len(self.queue) == self.size:
                # If the window is full, pop the oldest value from the left
                self.current_sum -= self.queue.popleft()
            # Add the new value to the window and update the sum
            self.queue.append(val)
            self.current_sum += val
            # Calculate the moving average
            return self.current_sum / len(self.queue)

## 3.Code Explanation:
# - The `__init__` method sets up the queue and initializes the variables to track the size of the window 
# and the current sum.
# - In the `next` method, if the window is already at the specified `size`, the oldest value is removed 
# from the queue, and its value is subtracted from `current_sum`. Then, the new value is added to the queue,
# and `current_sum` is updated to include the new value.
# - The average is calculated by dividing the `current_sum` by the current size of the queue (which reflects
# the number of elements within the window).

## 4.Time & Space Complexity:
# -Time Complexity: The time complexity for each call to `next` is O(1) because adding to and removing from
# a deque, as well as updating the current sum, are constant time operations.
# -Space Complexity: The space complexity is O(size) because the deque will hold at most `size` elements at
# any time, which corresponds to the size of the moving window.