#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(s="", open=0, close=0):
            # Base case: if we've used all parentheses, add to result
            if len(s) == 2 * n:
                result.append(s)
                return
            
            # We can add an opening parenthesis if we haven't used all n
            if open < n:
                backtrack(s + "(", open + 1, close)
            
            # We can add a closing parenthesis if we have more opening than closing
            if close < open:
                backtrack(s + ")", open, close + 1)
        
        # Start the backtracking process
        backtrack()
        return result
# @lc code=end

