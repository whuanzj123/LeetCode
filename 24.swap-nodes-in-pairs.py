#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: empty list or single node
        if not head or not head.next:
            return head
        
        # Create a dummy node to simplify handling the head
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize prev pointer to the node before each pair
        prev = dummy
        
        # Iterate while we have a pair to swap
        while head and head.next:
            # Define the two nodes to be swapped
            first = head
            second = head.next
            
            # Perform the swap (three-pointer manipulation)
            prev.next = second          # Link previous node to second node
            first.next = second.next    # Link first node to node after pair
            second.next = first         # Link second node to first node
            
            # Update pointers for next iteration
            prev = first                # Move prev to the end of the current pair
            head = first.next           # Move head to the start of the next pair
        
        return dummy.next
        
# @lc code=end

