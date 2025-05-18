from typing import List

# Problem: Permutations
# time complexity: O(n! * n) for generating all permutations
# n! for the number of permutations and n for copying the list
# space complexity: O(n! * n) for output list
#   and O(n) for the recursion stack
# The algorithm uses a depth-first search (DFS) approach to generate all possible permutations.
# The algorithm starts with an empty permutation and recursively adds each element to the permutation.
# The algorithm uses a backtracking approach to explore all possible combinations of elements.
# The algorithm also uses a swap operation to generate permutations in place.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i):
            if i == len(nums):
                res.append(nums.copy())
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        dfs(0)
        return res