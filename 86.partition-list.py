#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        point = head

        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        p1 = dummy1
        p2 = dummy2
        while point:
            if point.val >= x:
                p2.next = point
                p2 = p2.next
            else:
                p1.next = point
                p1 = p1.next
            
            point = point.next

        p2.next = None
        
        # Connect the first list to the second list
        p1.next = dummy2.next
        
        return dummy1.next




                



# @lc code=end

