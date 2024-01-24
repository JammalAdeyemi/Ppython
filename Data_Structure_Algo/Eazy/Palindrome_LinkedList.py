## Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Example 1:
        # Input: head = [1,2,2,1]
        # Output: true
        # Example 2:
        # Input: head = [1,2]
        # Output: false
        # Constraints:
        # The number of nodes in the list is in the range [1, 105].
        # 0 <= Node.val <= 9

# 1. Problem Understanding:
# • The challenge is to determine whether a singly linked list represents a sequence of values that reads the same 
# backward as forward, which defines a palindrome.
# • It's crucial to recognize that a list is a linear data structure without direct access to its middle or end, so 
# we must approach the problem creatively.
# • The constraint that we can only use O(1) additional space rules out converting the linked list into an array or 
# using a stack for comparison.

# 2. Algorithm Choice:
# • Two-Pointer Technique: Utilizing the fast and slow pointer approach allows us to find the middle of the list 
# without knowing the length beforehand.
# • List Reversal: Reversing the second half of the list in place enables us to compare it with the first half 
# without extra space.
# • Half-by-Half Comparison: By comparing nodes one by one from the start and from the middle to the end (reversed), 
# we can check for the palindrome property.

# 3. Implementation Details:
# • Middle Node Identification: Use the fast and slow pointers where the fast pointer moves twice as fast as the 
# slow pointer. When the fast pointer reaches the end of the list, the slow pointer will be at the middle.
# • Reversal of Second Half: Once the middle is found, reverse the second half of the list starting from the slow 
# pointer. This is achieved by reassigning the next pointer of each node to its previous node until all nodes in the
# second half are reversed.
# • Palindromic Check: With the reversed second half, compare the values of nodes starting from the head (first half) 
# and the nodes starting from the new head of the reversed second half. If all corresponding node values match, the 
# list is a palindrome. If any pair of nodes doesn't match, the list isn't a palindrome.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        Check if a singly linked list is a palindrome.
        :type head: ListNode
        :rtype: bool
        """
        # Find the middle of the linked list using the fast and slow pointer technique
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Compare the first half and the reversed second half
        left, right = head, prev
        while right:  # Only need to compare till the end of the shorter half
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        
        return True

#Time & Space Complexities
# • Time Complexity: O(n), where n is the number of nodes in the list. The list is traversed twice—once to find the 
# middle and once to compare the halves.
# • Space Complexity: O(1), as the reversal is done in place and no additional space that grows with the size of the
# input is used. We only use a few pointers for tracking the current node, the previous node, and the two halves for
# comparison.
        