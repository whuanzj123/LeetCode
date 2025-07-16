#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        left = nums[k]
        l = len(nums)
        for i in range(1,l):
            right = nums[i]
            if left != right:
                k += 1
                nums[k] = right
                left = nums[k]

        return k+1

# @lc code=end

