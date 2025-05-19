from typing import List
#
# Problem: Island Perimeter
# time complexity: O(n * m) where n is the number of rows and m is the number of columns
# space complexity: O(n * m) for the visited set
# This problem can also be solved using BFS or DFS
# but the DFS solution is more straightforward and easier to understand
# The algorithm uses a depth-first search (DFS) approach to explore the grid and calculate the perimeter of the island.
# The algorithm starts from the first land cell (1) and recursively explores its neighbors.
# The algorithm counts the number of edges that are adjacent to water (0) or out of bounds.
# The algorithm uses a visited set to keep track of the cells that have already been explored.
# The algorithm returns the total perimeter of the island.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if (r, c) in visited: return 0
            if r > ROWS - 1 or r < 0 or c > COLS - 1 or c < 0 or grid[r][c] == 0: 
                return 1
            visited.add((r, c))
            
            res = dfs(r + 0, c + 1) + dfs(r + 0, c + -1) + dfs(r + 1, c + 0) + dfs(r + -1, c + 0)
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)
                

# OPTIMAL SOLUTION in O(1) space complexity
# The optimal solution is to iterate through the grid and count the number of edges that are adjacent to water (0) or out of bounds.
# The algorithm uses a nested loop to iterate through each cell in the grid.
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += (i + 1 >= m or grid[i + 1][j] == 0)
                    res += (j + 1 >= n or grid[i][j + 1] == 0)
                    res += (i - 1 < 0 or grid[i - 1][j] == 0)
                    res += (j - 1 < 0 or grid[i][j - 1] == 0)
        return res