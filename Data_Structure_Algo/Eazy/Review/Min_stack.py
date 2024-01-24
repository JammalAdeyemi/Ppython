## Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# 1. MinStack() initializes the stack object.
# 2. void push(int val) pushes the element val onto the stack.
# 3. void pop() removes the element on the top of the stack.
# 4. int top() gets the top element of the stack.
# 5. int getMin() retrieves the minimum element in the stack.
#
# You must implement a solution with O(1) time complexity for each function.

## Intuition
# My immediate thought is to address the challenge of maintaining the minimum element in constant time, alongside the standard stack operations. The key intuition here is to use an auxiliary stack that parallels the main stack, but exclusively keeps track of the minimum elements. The beauty of this approach lies in its simplicity and efficiency. Each time we push a new element onto the main stack, we make a comparison with the current minimum. If it's smaller, or if our auxiliary 'min stack' is empty, this new element also gets pushed onto the min stack. This ensures that the top of the min stack always reflects the current minimum of our main stack.
# When popping an element, a simple check tells us if we're also removing the current minimum. If so, we pop from the min stack as well. This tandem operation between the two stacks is what allows us to retrieve the minimum element at any time in O(1) time complexity, harmoniously blending efficiency with functionality.
# I find this solution not only elegant but also very efficient, meeting the O(1) time complexity constraint for each stack operation, including retrieving the minimum element. It's like having a vigilant assistant (the min stack) alongside our main stack, always ready to tell us the smallest number without having to sift through the entire stack.

class MinStack(object):

    def __init__(self):
        # Initialize two stacks: one for storing all the values,
        # and another for keeping track of the minimum values.
        self.stack = []
        self.min = []
        
    def push(self, val):
        """
        Pushes an element onto the stack. 
        If the stack is empty or the value is less than the current minimum,
        it also gets added to the min stack for tracking the minimum value.
        :type val: int
        :rtype: None
        """
        self.stack.append(val) # push value onto main stack
        # Check if the min stack is empty or the current value is smaller than the last minimum.
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        
    def pop(self):
        """
        Removes the top element from the stack.
        Also removes the top element from the min stack if it's equal to the popped element.
        :rtype: None
        """
        # Check if the top element is the current minimum and pop it from the min stack.
        if self.stack: # check if main stack is not empty
            if self.stack[-1] == self.min[-1]:
                self.min.pop() # pop from minimum stack
            self.stack.pop() # always pop from main stack
        
    def top(self):
        """
        Returns the top element of the stack without removing it.
        :rtype: int
        """
        if self.stack: # Check if main stack is not empty
            return self.stack[-1] # return the top element
        
    def getMin(self):
        """
        Retrieves the minimum element from the stack.
        :rtype: int
        """
        if self.min:  # Check if the min stack is not empty
            return self.min[-1] # return the current minimum value

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()