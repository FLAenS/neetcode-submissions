class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [[1,0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        island = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
                return 
            grid[r][c] = "0"
            for dr, dc in dir:
                dfs(r + dr, c + dc)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    island += 1

        return island