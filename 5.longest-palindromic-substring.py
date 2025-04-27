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
        max_length = 1
        
        # Helper function to expand around center
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # Length of palindrome
        
        for i in range(len(s)):
            # Expand for odd-length palindromes (like "aba")
            len1 = expand_around_center(s, i, i)
            # Expand for even-length palindromes (like "abba")
            len2 = expand_around_center(s, i, i + 1)
            
            # Get the maximum length from the two expansions
            length = max(len1, len2)
            
            # Update the longest palindrome if a longer one is found
            if length > max_length:
                max_length = length
                # Calculate the starting position of the palindrome
                start = i - (length - 1) // 2
        
        return s[start:start + max_length]
        
# @lc code=end

