#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0:
            return False
        x = str(x)
        if len(x) % 2 != 0:
            i = 0
            while i < (len(x)-1)/2 and x[i] == x[len(x)-1-i]:
                i += 1
            if i != (len(x)-1)/2:
                return False
            return True
        else:
            i = 0 
            while i < len(x)/2 and x[i]==x[len(x)-1-i]:
                i += 1
            if i != (len(x))/2:
                return False
            return True                

        
        
# @lc code=end

