from typing import List
#
# Problem: Combination Sum
# time complexity: O(2^n) for all combinations
# space complexity: O(n) for the recursion stack
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        def dfs(i, count):
            if count == target:
                res.append(combination.copy())
                return
            if i >= len(nums) or count > target:
                return

            combination.append(nums[i])
            dfs(i, count + nums[i])
            combination.pop()
            dfs(i + 1, count)
        
        dfs(0, 0)            
        return res