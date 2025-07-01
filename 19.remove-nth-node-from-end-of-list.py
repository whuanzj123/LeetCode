#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = left.next
        for _ in range(n-1):
            right = right.next
        if not right:
            return head.next
        

        left = head
        right = left.next        
        while True:
            for _ in range(n):
                right = right.next
            if not right:
                left.next = left.next.next
                return head
            
            left = left.next
            right = left.next

        return head

# @lc code=end

