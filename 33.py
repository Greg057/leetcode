
# 33. Search in Rotated Sorted Array
# time complexity: O(log n) for binary search
# space complexity: O(1) for constant space

#  Explanation:
# 1. Find the pivot point where the array is rotated.
# 2. Use binary search to find the target in the appropriate half of the array.
# 3. If the target is not found, return -1.
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        
        l, r = 0, len(nums) - 1
        if nums[pivot] <= target and nums[r] >= target:
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
        

