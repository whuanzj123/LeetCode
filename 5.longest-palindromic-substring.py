#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        max_len = 1
        
        def expand_around_center(left: int, right: int) -> int:
            """Expand around center and return length of palindrome"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # Length of palindrome
        
        for i in range(len(s)):
            # Case 1: Odd length palindromes (center at i)
            len1 = expand_around_center(i, i)
            
            # Case 2: Even length palindromes (center between i and i+1)
            len2 = expand_around_center(i, i + 1)
            
            # Get the maximum length from both cases
            current_max = max(len1, len2)
            
            # Update global maximum if current is longer
            if current_max > max_len:
                max_len = current_max
                # Calculate start position based on center and length
                start = i - (current_max - 1) // 2
        
        return s[start:start + max_len]
# @lc code=end

