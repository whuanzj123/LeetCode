#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize dummy head for result linked list
        dummy_head = ListNode(0)
        current = dummy_head
        
        # Initialize carry
        carry = 0
        
        # Traverse both linked lists
        while l1 or l2:
            # Get values from nodes (or 0 if node doesn't exist)
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate sum with carry
            sum_val = x + y + carry
            
            # Update carry for next calculation
            carry = sum_val // 10
            
            # Create new node with ones digit
            current.next = ListNode(sum_val % 10)
            current = current.next
            
            # Move to next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # If there's a remaining carry, add a new node
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the head of the result list (skip dummy head)
        return dummy_head.next
        
# @lc code=end