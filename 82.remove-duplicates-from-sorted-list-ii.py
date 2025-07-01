#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = slow.next
        while fast:
            if fast and fast.next and fast.val == fast.next.val:
                while fast and fast.next and fast.val == fast.next.val:
                    fast = fast.next
                slow.next = fast.next
            else:
                fast = fast.next
                slow = slow.next



        return dummy.next
# @lc code=end

