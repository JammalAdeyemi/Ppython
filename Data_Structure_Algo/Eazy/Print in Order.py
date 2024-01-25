# Print in Order
# Suppose we have a class:
# public class Foo {
#  public void first() { print("first"); }
#  public void second() { print("second"); }
#  public void third() { print("third"); }
# }
# The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B
# will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure 
# that second() is executed after first(), and third() is executed after second().

# Note: We do not know how the threads will be scheduled in the operating system, even though the numbers in 
# the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

### Thought Process and Concepts Utilized
## Problem Understanding:
# -The problem presents a scenario where three methods (first, second, and third) of a class Foo are called 
# by three different threads (A, B, and C). The challenge is to ensure that these methods are executed in a
# specific order (first, then second, then third) regardless of the order in which threads are scheduled by
# the operating system.
# -This is a classic problem of thread synchronization where the execution order of code in different threads
# must be controlled.
# - The critical aspect to understand is that without proper synchronization mechanisms, threads can execute
# concurrently in an unpredictable order, leading to race conditions.

## Algorithm Choice:
# -Threading Events for Synchronization: The choice of using threading events (threading.Event()) in Python
# is based on their suitability for signaling between threads. An event can be used to block a thread until
# a certain condition is met (signaled by another thread).
# -Sequential Event Signaling: The implementation involves two events, first_done and second_done. The first
# method signals first_done upon completion, allowing the second method to proceed. Similarly, second signals
# second_done, allowing third to proceed.
# -Wait and Set Mechanism: Each method uses a wait call to wait for a signal from the preceding method. The
# set call is used to send a signal indicating the completion of the method. This mechanism effectively enforces
# the required execution order.
# -Simple and Effective Synchronization: This solution is chosen for its simplicity and effectiveness in 
# solving the problem of controlling the execution order in a multi-threaded environment. It avoids more 
# complex synchronization mechanisms like locks or semaphores, which might be overkill for this specific 
# problem.

import threading
class Foo(object):
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # Signal that first() is done
        self.first_done.set()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        # Wait until first() is done  
        self.first_done.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        # Signal that second() is done
        self.second_done.set()
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        # Wait until second() is done
        self.second_done.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

## Explanation
# -Thread Synchronization: Two threading.Event objects, first_done and second_done, are used to synchronize
# the order of method execution.
# -first Method: Executes printFirst and then sets the first_done event to signal that the first method has
# completed.
# -second Method: Waits for the first_done event (using self.first_done.wait()) before executing printSecond. 
# This ensures that second will not execute until first is done. After executing printSecond, it sets the 
# second_done event.
# -third Method: Waits for the second_done event before executing printThird, ensuring that it runs after 
# second.

## Time & Space Complexities
# -Time Complexity: The actual complexity depends on the scheduling of threads by the OS, but the design ensures
# the methods execute in the correct order (first, then second, then third).
# -Space Complexity: O(1) as only two event objects are used, regardless of the input size.
