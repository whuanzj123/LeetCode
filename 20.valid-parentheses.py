#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack to keep track of opening brackets
        stack = []
        
        # Create a mapping of closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        
        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element if the stack is not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the corresponding opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were correctly matched
        # If not empty, there are unmatched opening brackets
        return not stack
# @lc code=end

