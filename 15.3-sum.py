#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two-pointer approach for the remaining array
            left, right = i + 1, n - 1
            target = -nums[i]  # We want the triplet to sum to 0
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum < target:
                    left += 1  # Sum too small, increase left pointer
                elif current_sum > target:
                    right -= 1  # Sum too large, decrease right pointer
                else:
                    # Found a triplet!
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers
                    left += 1
                    right -= 1
        
        return result
        
# @lc code=end

