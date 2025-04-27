#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        thousands = num // 1000
        roman += thousands * 'M'
        hundreds = (num // 100) % 10
        if hundreds == 9:
            roman += 'CM'
        elif hundreds == 4:
            roman += 'CD'
        else:
            roman += (hundreds // 5)*'D' + (hundreds % 5)*'C'
        tens = (num // 10) % 10 
        if tens == 9:
            roman += 'XC'
        elif tens == 4:
            roman += 'XL'
        else:
            roman += (tens // 5)*'L' + (tens % 5)*'X'
        ones = num % 10 
        if ones == 9:
            roman += 'IX'
        elif ones == 4:
            roman += 'IV'
        else:
            roman += (ones // 5)*'V' + (ones % 5)*'I'
        return roman            

# @lc code=end

