## Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

## Thought Process and Concepts Utilized
# 1. Problem Understanding:
# - The task is to reverse a singly linked list, where each node points to the next node, and the list ends with a 
# `None`.
# - The goal is to make each node point to its previous node instead of the next one, effectively reversing the 
# direction of the list.
# - The head of the original list becomes the tail of the reversed list, and the original tail becomes the new head.

# 2. Algorithm Choice:
# - Iterative Approach: This approach uses a loop to traverse the list once, changing the `next` pointers of each 
# node to reverse the list.
# - Pointer Manipulation: Two pointers are used – one to keep track of the current node being processed (`curr`) 
# and the other to keep track of the previous node (`prev`).

# 3. Implementation Details:
# - Initialization: Two pointers, `prev` (initialized to `None`) and `curr` (initialized to `head`), are used.
# - Traversing the List: The algorithm iterates over the list using `curr`. In each iteration, it:
    # - Temporarily stores the next node (`next_node = curr.next`).
    # - Reverses the `curr` node’s `next` pointer to point to `prev`.
    # - Advances `prev` and `curr` to the next positions (`prev = curr`, `curr = next_node`).
# - New Head: When `curr` reaches the end of the list (`None`), `prev` is at the new head of the reversed list.

# 4. Time & Space Complexities:
# - Time Complexity: O(n), where `n` is the number of nodes in the list. The algorithm traverses the list once, 
# processing each node a single time.
# - Space Complexity: O(1), as the reversal is done in-place. The space used does not depend on the size of the 
# input list, only on a fixed number of pointers.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Iterative
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Initialize previous and current pointers
        prev = None
        curr = head
        # Iterate over the linked list
        while curr:
            # Remember the next node
            next_node = curr.next
            # Reverse the direction of the current node
            curr.next = prev
            # Move the previous and current pointers one step forward
            prev = curr
            curr = next_node
        # At the end, prev will be the new head of the reversed list
        return prev

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?   
## Recursive
# class Solution:
#     def reverseListRecursive(self, head):
#         # Base case: If head is empty or has reached the list's end
#         if not head or not head.next:
#             return head
#         # Recursive case: Reverse the rest of the list
#         recurse = self.reverseListRecursive(head.next)
        
#         # Set the next node's next to the current head
#         head.next.next = head
#         # Set the head's next to None
#         head.next = None

#         return recurse

## Explanation of Recursive Approach
# • Base Case: When the current node is None or it is the last node (head.next is None), we have reached the end of 
# the list, and we return the current node.
# • Recursive Step: Recursively call reverseListRecursive for head.next, which will eventually return the new head 
# of the reversed list.
# • Reversing the Pointers: As the stack unwinds, set the next node's next pointer to the current node (head). This 
# reverses the link.
# • Setting Head's Next to None: Finally, set head.next to None to break the original link and avoid cycles.

## Time & Space Complexities
# Recursive Approach:
# • Time Complexity: O(n) - each node is visited once.
# • Space Complexity: O(n) - due to recursive stack space in the worst case (when the list is not shallow).