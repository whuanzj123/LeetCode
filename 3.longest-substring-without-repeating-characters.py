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
        length = float('inf')
        while right <= len(s)-1:
            right += 1
            move = s[right]
            if move not in s[left:right]:
                if right - left + 1 < length:
                    length = right - left + 1

            while s[right] in s[left:right]:
                out = s[left]
                left += 1

            return length
            

# @lc code=end

