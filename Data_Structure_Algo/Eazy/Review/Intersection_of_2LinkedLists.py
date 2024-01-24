## Intersection of Two Linked Lists
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.

### Thought Process and Concepts Utilized
# 1. Problem Understanding:
# - The objective is to identify a node at which two singly linked lists intersect.
# - It's understood that the intersection means the nodes are the same by reference, not just by value.
# - The challenge is to find the intersection efficiently without modifying the linked lists or using extra space.

# 2. Algorithm Choice:
# - Two Pointer Approach: The two-pointer technique is chosen because it is space-efficient and only requires 
# O(n + m) time.
# - List Concatenation Insight: This approach leverages the insight that by switching pointers to the head of the 
# opposite list after reaching the end, both pointers will sync up at the intersection point on their second pass through the lists.

# 3. Implementation Details:
# - Pointer Initialization: Start with two pointers, each at the head of one list.
# - Pointer Traversal: Traverse through the lists, advancing the pointers one node at a time.
# - Switching Heads: When a pointer reaches the end of a list, move it to the head of the other list.
# - Intersection Detection: The loop continues until the two pointers either meet at the intersection node or both 
# reach the end (`None`).

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        Find the node where two singly linked lists intersect.
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Initialize two pointers for both lists
        pointerA, pointerB = headA, headB
        # Iterate through both lists
        while pointerA is not pointerB:
            # When pointerA reaches the end of listA, redirect it to the head of listB
            pointerA = pointerA.next if pointerA else headB
            # When pointerB reaches the end of listB, redirect it to the head of listA
            pointerB = pointerB.next if pointerB else headA
        # The pointers will either meet at the intersection node or at the end (None)
        return pointerA
## Explanation
# • Two Pointers: One pointer starts at the head of listA, and the other at the head of listB.
# • Traversing the Lists: Each pointer moves through the list it's currently on, node by node.
# • Switching Lists: When a pointer reaches the end of a list, it switches to the head of the other list.
# • Meeting Point: If the lists intersect, the pointers will meet at the intersection node after traversing at most 
# lengthA + lengthB nodes. If they do not intersect, both pointers will eventually be None at the same time, exiting
# the loop.
# • Return Node: The method returns the node where the two pointers meet, which is either the intersection node or 
# None.

## Time & Space Complexities
# • Time Complexity: O(n + m), where n is the length of listA and m is the length of listB. Each pointer traverses 
# at most two lists.
# • Space Complexity: O(1), as no additional space is allocated; the space used is constant, regardless of the size 
# of the input lists.

## Summary
# The algorithm is elegantly designed to solve the problem without needing extra space and without altering the 
# input lists. The two-pointer technique is particularly effective here because it ensures that each pointer 
# traverses each list only once, guaranteeing that they will align at the intersection point if one exists. This 
# method is a classic example of algorithmic ingenuity, utilizing the inherent structure of the problem to find a 
# solution that is both simple and efficient.