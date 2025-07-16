#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for i in t:
            need[i] = need.get(i, 0) + 1

        window ={}
        left = 0
        right = 0
        valid = 0

        while right <= len(s)-1 and valid < len(t):
            move = s[right]

            if move in t:
                window[move] = window.get(move,0)+1

                if window[move] == need[move]:
                    valid += 1
            right += 1

        if valid < len(t):
            return ""
        
        while True:
            out = s[left]

            if out in t:
                window[move] = window.get(move) - 1

                if window[move] < need[move]:
                    return s[left:right+1]
        

            

# @lc code=end

