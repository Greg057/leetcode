from typing import List
#
# Problem: Jump Game
# time complexity: O(n) for linear scan
# space complexity: O(1) for constant space
# Greedy approach: We can start from the end of the array and check if we can reach the last index from each index.
# If we can reach the last index from the current index, we update the goal to the current index.
# If we reach the first index, we can jump to the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0