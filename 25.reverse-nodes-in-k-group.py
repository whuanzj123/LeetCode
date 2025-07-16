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

        flag1 = dummy
        flag2 = head
        previous = head
        current = previous.next
        
        while current:

            for i in range(k-1):
                if current:
                    nextone = current.next

                else:
                    # restore reserved node when not enough node
                    for j in range(i):
                        restoreflag = previous.next

                        previous.next = current
                        current = previous
                        previous = restoreflag
                    return dummy.next
                current.next = previous
                previous = current
                current = nextone

            flag1.next = previous
            flag2.next = current

            flag1 = flag2
            previous = current
            flag2 = current


            # hanlde some edge cases
            if current:
                current = current.next
            else:
                return dummy.next
        return dummy.next






        
# @lc code=end

