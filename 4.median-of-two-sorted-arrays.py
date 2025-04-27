#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the shorter array for simplicity
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            # Partition points
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # If partitionX is 0, use -infinity for maxX
            # If partitionX is x, use infinity for minX
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            
            # Similarly for Y
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]
            
            if maxX <= minY and maxY <= minX:
                # We found the correct partition
                # If total length is odd
                if (x + y) % 2 != 0:
                    return max(maxX, maxY)
                else:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
            elif maxX > minY:
                # Move partition to the left in X
                high = partitionX - 1
            else:
                # Move partition to the right in X
                low = partitionX + 1
                
        # If we get here, input arrays weren't sorted
        raise ValueError("Input arrays are not sorted")
# @lc code=end

