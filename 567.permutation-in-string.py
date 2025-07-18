#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        right = 0
        left = 0
        need = {}
        for i in s1:
            need[i] = need.get(i, 0) + 1

        while right <= len(s2)-1:
            window = {}
            valid = 0
            left = right
            while right <= len(s2)-1 and s2[right] in s1:
                move = s2[right]
                window[move] = window.get(move,0) + 1
                if window[move] == need[move]:
                    valid +=1 
                    if valid == len(need):
                        return True
                elif window[move] > need[move]:
                    while s2[left] != move:
                        left += 1
                    right = left
                    break

                right += 1
            right += 1        
        return False


# @lc code=end

