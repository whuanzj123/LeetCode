#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store values we've seen and their indices
        seen = {}  # value: index
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement (the number we need to find)
            complement = target - num
            
            # If the complement exists in our map, we found our answer
            if complement in seen:
                return [seen[complement], i]
                
            # Otherwise, add the current number to our map
            seen[num] = i
            
        # Problem guarantees a solution, so we shouldn't reach here
        return []        
        
# @lc code=end

