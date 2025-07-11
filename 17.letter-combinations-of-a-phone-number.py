#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        diction = {'2':['a','b','c'],
                   '3':['d','e','f'],
                   '4':['g','h','i'],
                   '5':['j','k','l'],
                   '6':['m','n','o'],
                   '7':['p','q','r','s'],
                   '8':['t','u','v'],
                   '9':['w','x','y','z']}

        n = len(digits)
        result = [""]
        # for i in range(len(diction[digits[0]])):
        #     result.append("")
        for i in range(n):
            l = len(diction[digits[i]])
            temp = []
            for m in range(len(result)):
                for n in range(l):
                    temp.append(result[m]+diction[digits[i]][n])
            result = temp

        return result



        
        
# @lc code=end

