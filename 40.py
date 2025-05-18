
from typing import List
# Problem: Combination Sum II
# time complexity: O(2^n) for all combinations
# space complexity: O(n) for the recursion stack
# Note: The input list may contain duplicates, so we need to handle that in our implementation.
# The algorithm uses a depth-first search (DFS) approach to generate all possible combinations.
# The algorithm starts with an empty combination and recursively adds each element to the combination or skips it.
# The algorithm uses a backtracking approach to explore all possible combinations of elements.
# The algorithm also sorts the input list to handle duplicates and avoid generating duplicate combinations.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)
        return res