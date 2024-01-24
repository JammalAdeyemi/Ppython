## Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, 
# and return the new head.

## Thought Process and Concepts Utilized
# 1. Problem Understanding:
# • The task is to remove all nodes from a linked list that have a specific value (val).
# • The linked list is a singly-linked list where each node points to the next node.
# • The function should return the new head of the modified linked list.

# 2. Algorithm Choice:
# • Traversing the Linked List: Since linked lists are linear data structures, the solution requires traversing the 
# list from the head to the end.
# • Pointer Manipulation: The core of solving this problem lies in correctly manipulating the pointers of the nodes 
# to 'skip' the nodes that need to be removed.

# 3. Implementation Details:
# • Dummy Node: Introducing a dummy node as a new head of the list. This simplifies handling cases where the head 
# itself needs to be removed.
# • Current Node Pointer: Using a pointer (current) to traverse the list. This pointer always points to the node 
# just before the node under consideration.
# • Removal Logic: If the next node of current has the value val, it is removed by setting current.next to 
# current.next.next.
# • Traversal Continuation: If the next node does not need to be removed, simply move the current pointer to the 
# next node.

# 4. Edge Cases:
# • Empty List: If the head is None, the list is empty, and there's nothing to remove.
# • Removing Head Node(s): If the head node (or several starting nodes) has the value val, these nodes need to be 
# removed. The dummy node simplifies this process.
# • Consecutive Nodes with Target Value: Consecutive nodes with the value val require careful pointer adjustment to 
# ensure all such nodes are removed.
# • No Nodes to Remove: If no nodes have the value val, the original list should be returned as-is.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Initialize a dummy node that points to the head of the list
        # This helps to easily handle edge cases like removing the head node itself
        dummy = ListNode(next=head)

        # Initialize the current node to the dummy and the next node to the head
        current = dummy

        # Iterate through the linked list
        while current.next:
            # If the next node's value is the one to remove
            if current.next.val == val:
                # Remove the node by linking current node to next of next node
                current.next = current.next.next
            else:
                # Move to the next node in the list
                current = current.next

        # Return the new head of the list, which is next of the dummy node
        return dummy.next