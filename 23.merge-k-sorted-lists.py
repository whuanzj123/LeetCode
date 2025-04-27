#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            # Create a dummy head to simplify edge cases
            dummy = ListNode(-1)
            current = dummy
            
            # Use two pointers to iterate through both lists
            while list1 and list2:
                # Compare values and take the smaller one
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                
                # Move the current pointer forward
                current = current.next
            
            # If one list is exhausted, append the remainder of the other list
            current.next = list1 if list1 else list2
            
            # Return the merged list (excluding the dummy head)
            return dummy.next
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]

        k = mergeTwoLists(list1=lists[0], list2=lists[1])
        for i in range(1,len(lists)-1):
            k = mergeTwoLists(k, lists[i+1])

        return k
# @lc code=end

