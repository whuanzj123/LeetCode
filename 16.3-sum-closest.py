#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array
        n = len(nums)
        closest_sum = float('inf')  # Initialize with infinity
        
        for i in range(n - 2):  # Fix the first element
            # Use two pointers for the remaining elements
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Adjust pointers based on comparison with target
                if current_sum < target:
                    left += 1  # Need a larger sum, move left pointer right
                elif current_sum > target:
                    right -= 1  # Need a smaller sum, move right pointer left
                else:
                    # Found exact match, return immediately
                    return target
        
        return closest_sum        
# @lc code=end

