## Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two 
# lists.
# Return the head of the merged linked list.

## Thought Process
# Problem Understanding
# - The task is to merge two sorted singly linked lists (`list1` and `list2`) into one sorted linked list.
# - The merging should be done by splicing together the nodes of the two lists, without creating new nodes.
# - The merged list should be sorted, maintaining the original sorting order of `list1` and `list2`.

# Algorithm Choice
# - Iterative Merge: The chosen algorithm iteratively compares nodes from both lists and appends the smaller node to the merged list. This approach is efficient for sorted lists as it leverages their existing order.
# - Dummy Head Node: Using a dummy head node simplifies handling edge cases, such as when one of the lists is initially empty.

# Implementation Details
# - Initialization: A dummy node `dummy` is created to act as the starting point of the merged list. A separate `head` pointer is used to store the beginning of the merged list (which will be `dummy.next`).
# - Iterating Over Lists: The algorithm iterates over both `list1` and `list2` as long as neither is exhausted. In each iteration, it:
  # - Compares the values of the current nodes of `list1` and `list2`.
  # - Appends the node with the smaller value to the `dummy` node.
  # - Advances the `dummy` pointer and the pointer of the list from which the node was taken.
# - Appending Remaining Nodes: After exiting the loop (when one of the lists is exhausted), the remaining part of the non-exhausted list (if any) is appended to the merged list.
# - Returning the Merged List: The function returns `head.next`, which is the start of the merged list (excluding the dummy node).

# Time & Space Complexities
# - Time Complexity**: O(n + m), where `n` is the length of `list1` and `m` is the length of `list2`. This is because, in the worst case, the algorithm iterates through all nodes of both lists once.
# - Space Complexity: O(1), as the merge is done in-place. The only additional space used is for the dummy node and a few pointers, which is constant and does not depend on the size of the input lists.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize a dummy node to build the merged list
        dummy = ListNode()
        head = dummy  # 'head' keeps a reference to the start of the merged list

        # Iterate while both lists have nodes
        while list1 and list2:
            # Select the node with the smallest value
            if list1.val < list2.val:
                dummy.next = list1  # Add the selected node into the merged list
                list1 = list1.next  # Move the pointer to the next node in list1
            else:
                dummy.next = list2  # Add the selected node into the merged list
                list2 = list2.next  # Move the pointer to the next node in list2
                
            dummy = dummy.next  # Move the pointer of the merged list to the next node

        # Attach the remaining part of list1 or list2, if any    
        dummy.next = list1 if list1 else list2
        # Return the head of the merged list, excluding the dummy node
        return head.next  