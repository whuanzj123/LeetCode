#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        # Step 1: Ignore leading whitespace
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Check if we've reached the end of the string
        if i == len(s):
            return 0
        
        # Step 2: Determine the sign
        sign = 1
        if s[i] == '-' or s[i] == '+':
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Read the integer
        result = 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        # Apply the sign
        result = sign * result
        
        # Step 4: Check for range and clamp if necessary
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
        
# @lc code=end

