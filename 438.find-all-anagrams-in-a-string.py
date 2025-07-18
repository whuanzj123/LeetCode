#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        results = []
        left = 0
        right = 0
        need = {}
        for i in p:
            need[i] = need.get(i, 0) + 1
        window = {}
        valid = 0

        while right <= len(s) - 1:
            move = s[right]
            right += 1
            if move in p:
                window[move] = window.get(move, 0) + 1
                if window[move] == need[move]:
                    valid += 1

            if right - left + 1 > len(p):
                if valid == len(need):
                    results.append(left)
                out = s[left]
                if out in p:
                    if window[out] == need[out]:
                        valid -= 1
                    window[out] -= 1
                    
                left += 1 
        return results



# @lc code=end

