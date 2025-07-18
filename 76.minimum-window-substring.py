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
        length = float('inf')
        while right <= len(s)-1:
            move = s[right]
            if move in t:
                window[move] = window.get(move,0)+1

                if window[move] == need[move]:
                    valid += 1

            while valid == len(need):
                out = s[left]
                if out in t:
                    window[out] = window.get(out) - 1
                    if window[out] < need[out]:
                        valid -= 1
                left += 1
                if right - (left-1) < length:
                    start = left -1
                    end = right
                    length = right - (left-1)
            
            right += 1

        if length == float('inf'):
            return ""
        return s[start:end+1]
            


            

            

# @lc code=end

