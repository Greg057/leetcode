from typing import List
# Problem: Maximum Subarray
# time complexity: O(n) for linear scan
# space complexity: O(1) for constant space
# This problem is a classic example of Kadane's algorithm, which is used to find the maximum sum of a contiguous subarray in an array of integers.
# The algorithm works by maintaining a running sum of the current subarray and updating the maximum sum found so far.
# The key idea is to reset the running sum to zero whenever it becomes negative, as a negative sum would not contribute positively to any future subarray.
# The algorithm iterates through the array, adding each element to the running sum and checking if it exceeds the maximum sum found so far.
# If the running sum becomes negative, it is reset to zero.
# The final result is the maximum sum found during the iteration.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        total = 0
        for n in nums:
            if total < 0:
                total = 0
            total += n
            maxSum = max(maxSum, total)
        return maxSum