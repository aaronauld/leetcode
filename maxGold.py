class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(i, j, g):
            # check that current position is in grid and has gold
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
                return g
                # do not check a position that was already visted during the current DFS
            if grid[i][j] == "#":
                return g

                # add the gold at this position to the current total
            g += grid[i][j]

            # mark this position as visited
            temp = grid[i][j]
            grid[i][j] = "#"

            # run DFS on all the neighbors and take the max amount of gold
            g = max(dfs(i+1, j, g), dfs(i-1, j, g),
                    dfs(i, j+1, g), dfs(i, j-1, g))

            # reset the curr grid position gold amount so it may be visited from different DFS paths
            grid[i][j] = temp

            return g

        ans = 0
        # loop through each grid space and check if it has gold, if so, run DFS
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                    # keep track of which DFS produced the max amount of gold
                ans = max(ans, dfs(i, j, 0))

        return ans
