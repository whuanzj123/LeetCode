#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # 32-bit integer limits
        INT_MAX = 2**31 - 1  # 2,147,483,647
        
        # Handle the sign
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        
        # Reverse the digits
        reversed_x = 0
        while x > 0:
            # Extract the last digit
            last_digit = x % 10
            x //= 10
            
            # Check for potential overflow before adding digit
            if reversed_x > INT_MAX // 10 or (reversed_x == INT_MAX // 10 and last_digit > 7):
                return 0
            
            # Add the digit to the reversed number
            reversed_x = reversed_x * 10 + last_digit
        
        # Apply the sign
        return sign * reversed_x
        
# @lc code=end

