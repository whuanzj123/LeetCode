#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1

        while i < j:
            k = s[i]
            s[i] = s[j]
            s[j] = k

            i += 1
            j -= 1
# @lc code=end

