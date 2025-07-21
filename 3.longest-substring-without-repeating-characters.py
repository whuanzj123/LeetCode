#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        length = 0

        while right <= len(s)-1:
            move = s[right]
            right += 1

            while move in s[left:right-1]:
                left += 1

            if right - left > length:
                length = right - left
        
        return length
            

# @lc code=end

