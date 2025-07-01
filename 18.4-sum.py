#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        target_all = target
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left, right = j+1, n-1
                target = -nums[j]-nums[i] + target_all

                while left < right:
                    current_sum = nums[left] + nums[right]

                    if current_sum < target:
                        left += 1
                    elif current_sum > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for third element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for fourth element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move both pointers
                        left += 1
                        right -= 1

        return result
# @lc code=end

