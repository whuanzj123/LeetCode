#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}  # Dictionary to store the most recent position of each character
        max_length = 0  # To track the maximum length found
        start = 0       # Start of the current window
        
        for end in range(len(s)):
            # If the current character is in the dictionary and its position is >= start
            if s[end] in char_dict and char_dict[s[end]] >= start:
                # Move the start pointer to the position after the last occurrence
                start = char_dict[s[end]] + 1
            else:
                # Update max_length if the current window is larger
                max_length = max(max_length, end - start + 1)
            
            # Update the position of the current character
            char_dict[s[end]] = end
        
        return max_length
        
# @lc code=end

