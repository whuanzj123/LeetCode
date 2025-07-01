#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a DP table where dp[i][j] represents if s[0...i-1] matches p[0...j-1]
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: empty pattern matches empty string
        dp[0][0] = True
        
        # Handle patterns like "a*b*c*" that can match empty string
        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]  # Skip both '*' and the preceding character
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    # Two cases for '*':
                    # 1. Ignore the '*' and the preceding element (count it as zero)
                    dp[i][j] = dp[i][j-2]
                    
                    # 2. Use the '*' to match the current character in s
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]  # Use previous match and extend
                else:
                    # For non-'*' characters, simple match
                    if p[j-1] == '.' or p[j-1] == s[i-1]:
                        dp[i][j] = dp[i-1][j-1]
        
        return dp[len(s)][len(p)]
        
# @lc code=end

