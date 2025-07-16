#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        left = numbers[i]
        right = numbers[j]

        while True:
            if left + right < target:
                i += 1
                left = numbers[i]

            elif left + right > target:
                j -= 1
                right = numbers[j]

            else:
                return [i+1,j+1]
# @lc code=end

