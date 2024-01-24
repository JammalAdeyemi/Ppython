# Design an Ordered Stream
# There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.
# Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.
# Implement the OrderedStream class:
# -OrderedStream(int n) Constructs the stream to take n values.
# -String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.

### Thought Process and Concepts Utilized
## 1.Problem Understanding:
# -The challenge is to design an `OrderedStream` that handles a series of `(idKey, value)` pairs, with `idKey` 
# being an integer between 1 and `n`. The critical aspect is that these pairs may arrive in any order, and 
# the goal is to output the values in increasing order of their `idKey`s.
# -The stream should return chunks of values that are sequentially ordered by their `idKey`s, starting from
# the lowest `idKey` not yet outputted.
# -A unique aspect of the problem is that the chunks of values returned after each insertion must be 
# contiguous and in order, making it different from just sorting and returning values.

## 2. Algorithm Choice:
# -List for Stream Storage: A list is chosen to store the values at their respective `idKey` positions. 
# This approach allows direct access to values based on `idKey` and simplifies the process of determining 
# when a contiguous sequence of values is ready for output.
# -Pointer for Tracking Order: A pointer (`ptr`) is used to keep track of the next `idKey` expected to be 
# inserted. This pointer is essential for determining when a sequence of contiguous values starts and 
# helps in deciding whether to return a chunk or an empty list.
# -Dynamic Chunk Assembly: The solution includes dynamically assembling chunks of contiguous values 
# starting from the `ptr`. This assembly occurs during each `insert` operation and depends on whether the 
# inserted `idKey` matches the expected `idKey`.
# -Immediate Output After Insertion: The design choice ensures that after each insertion, the method 
# immediately checks and outputs a contiguous chunk of values (if available), adhering to the problem's 
# requirement of returning chunks after each insertion.
   

class OrderedStream:

    def __init__(self, n):
        """
        Initializes the OrderedStream to take n values.
        :type n: int
        """
        self.stream = [None] * (n + 1)  # +1 as the idKey starts from 1
        self.ptr = 1  # Pointer to the next expected idKey

    def insert(self, idKey, value):
        """
        Inserts the pair (idKey, value) into the stream.
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.stream[idKey] = value  # Insert the value at its idKey position

        if idKey == self.ptr:
            # Find the next chunk of continuous non-None values
            chunk = []
            while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
                chunk.append(self.stream[self.ptr])
                self.ptr += 1
            return chunk
        else:
            # If the idKey is not the next expected, return an empty list
            return []

## Explanation
# -Initialization (`__init__`): The constructor initializes a list `self.stream` to hold the values. The 
# list's size is `n + 1` since `idKey` starts from 1. The `self.ptr` variable tracks the next expected 
# `idKey`.
# -Insert Method (`insert`):
    # -The method places the `value` in `self.stream` at the index `idKey`.
    # -If `idKey` is the next expected one (`self.ptr`), it collects a chunk of continuous non-None values 
    # starting from `idKey` and updates `self.ptr` to point to the next expected `idKey`. 
    # -If `idKey` is not the next expected, it returns an empty list since we cannot form a continuous 
    # chunk from `self.ptr`.

## Time & Space Complexities
# -Time Complexity:
    #- `__init__`: O(n), as we initialize a list of size `n + 1`.
    #- `insert`: O(k) for each insert operation, where `k` is the number of continuous non-None values 
    # found. In the worst case, it could be O(n), but typically much less.
# -Space Complexity: O(n), used by the `self.stream` list to store the `n` values.
