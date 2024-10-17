"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(grid, r, c):
            # if its out of bound or is water, we want to stop our dfs
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"        # we know its part of the island because we can reach it from another part of the island in dfs
                                    # so just make it water
            dfs(grid, r+1, c)       # visit the neighbors recursively
            dfs(grid, r-1, c)
            dfs(grid, r, c+1)
            dfs(grid, r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands+=1
                    dfs(grid, r, c)
        return islands