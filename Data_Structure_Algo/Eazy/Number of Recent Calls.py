# Number of Recent Calls
# You have a RecentCounter class which counts the number of recent requests within a certain time frame.
# Implement the RecentCounter class:
# • RecentCounter() Initializes the counter with zero recent requests.
# • int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns
# the number of requests that has happened in the past 3000 milliseconds (including the new request). 
# Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

### Thought Process and Concepts Utilized
#1. Problem Understanding:
# -The task is to create a `RecentCounter` class that tracks the number of requests within a recent time 
# frame of 3000 milliseconds.
# -Each new request is timestamped, and only those within the 3000 millisecond window from the current 
# request need to be counted.
# -The main challenge is efficiently adding new timestamps and removing old ones that fall outside the 
# relevant time frame.

# 2.Algorithm Choice:
# -Queue Data Structure: Given the nature of the problem (first-in, first-out), a queue is a suitable data
# structure for storing timestamps. In Python, this can be implemented using a list.
# -Dynamic Window Management: The solution needs to dynamically adjust the time window as new requests come
# in, which involves adding new timestamps to the queue and removing old ones that are no longer within the
# 3000 millisecond window.

class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        # Remove timestamps older than 3000 milliseconds from t
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        return len(self.requests)
        
# Explanation
# • Initialization (__init__): Initialize an empty list self.requests to store the timestamps of each request.
# • Method ping:
    # -Add the new timestamp t to self.requests.
    # -Remove timestamps from the start of the queue that are older than 3000 milliseconds from t. This is 
    # done in a while loop, which checks and pops the oldest timestamp until the oldest timestamp is 
    # within the 3000 millisecond window.
    # -Return the number of elements in self.requests, which represents the number of recent requests 
    # within the past 3000 milliseconds.

# Time & Space Complexities
# -Time Complexity: Each call to ping is O(n) in the worst case, where n is the number of elements to 
# remove from the start of the list (when using a list as a queue).
# -Space Complexity: O(n), where n is the number of requests that occur within a 3000 millisecond window, 
# as we store each of these timestamps in the self.requests list.