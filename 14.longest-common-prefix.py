#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def string_difference(a, b):
            # Find the common prefix
            common_length = 0
            for i in range(min(len(a), len(b))):
                if a[i] != b[i]:
                    break
                common_length += 1
            
            return a[:common_length]
        
        if len(strs)<2:
            return strs[0]
        k = string_difference(strs[0], strs[1])
        for i in range(2,len(strs)):
            k = string_difference(strs[i], k)

        return k
        


        
# @lc code=end

