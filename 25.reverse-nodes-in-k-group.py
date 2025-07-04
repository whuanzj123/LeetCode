#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], 
                      k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        previous = head
        current = previous.next
        while current:
            for i in range(k):

        
# @lc code=end

