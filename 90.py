from typing import List
# problem: 90. Subsets II
# time complexity: O(n * 2^n) for generating all subsets
# Explanation solution:
# The algorithm uses a depth-first search (DFS) approach to generate all possible subsets.
# The algorithm starts with an empty subset and recursively adds each element to the subset or skips it.
# The algorithm uses a backtracking approach to explore all possible combinations of elements.
# The algorithm also sorts the input list to handle duplicates and avoid generating duplicate subsets.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []

        def dfs(i):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res

