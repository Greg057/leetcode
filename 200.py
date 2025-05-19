from typing import List
#
# Problem: Number of Islands
# time complexity: O(m * n) where m is the number of rows and n is the number of columns
# space complexity: O(m * n) for the recursion stack
# This is a DFS solution to count the number of islands in a grid.
# The algorithm uses a depth-first search (DFS) approach to explore the grid and count the number of islands.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
                return
            grid[r][c] = '0'

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands