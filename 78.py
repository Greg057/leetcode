from typing import List
# Problem: Subsets
# time complexity: O(2^n) for generating all subsets
# space complexity: O(n) for storing the subset
# Note: The space complexity is O(n) for the recursion stack, but the overall space complexity is O(2^n)
# because we are generating all subsets.
# The number of subsets of a set with n elements is 2^n.
# The number of subsets is 2^n because each element can either be included or excluded from a subset.
# The solution uses a depth-first search (DFS) approach to generate all possible subsets.
# The algorithm starts with an empty subset and recursively adds each element to the subset or skips it.
# The algorithm uses a backtracking approach to explore all possible combinations of elements.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
    