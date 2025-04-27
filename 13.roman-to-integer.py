#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        dict={
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        while len(s)>=2:
            if symbols.index(s[0]) <= symbols.index(s[1]):
                result += dict[s[0]]
                s = s[1:]
            else:
                result += dict[s[0:2]]
                s = s[2:]
        if s:
            result += dict[s[0]]
        return result

        
# @lc code=end

