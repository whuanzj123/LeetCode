#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s, numRows):
        # Handle edge cases
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array of strings for each row
        rows = [''] * numRows
        
        row = 0
        step = 1  # 1 for moving down, -1 for moving up
        
        for char in s:
            # Add the current character to the current row
            rows[row] += char
            
            # Change direction if we've reached the boundary
            if row == 0:
                step = 1  # Start moving down
            elif row == numRows - 1:
                step = -1  # Start moving up
            
            # Move to the next row
            row += step
        
        # Combine all rows into a single string
        return ''.join(rows)
            
# @lc code=end

