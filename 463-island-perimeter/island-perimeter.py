class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # ans = 0
        # def inbound(ri, ci):
        #     return 0 <= ri < len(grid) and 0 <= ci < len(grid[0])
        # for i, row in enumerate(grid):
        #     for j, ce in enumerate(row):
        #         if ce == 1:
        #             ans += 4
        #             for x, y in directions:
        #                 if inbound(i + x, j + y) and grid[i + x][j + y]:
        #                     ans -= 1
        # return ans
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        def inbound(ri, ci):
            return 0 <= ri < rows and 0 <= ci < cols

        def dfs(ri, ci):
            if not inbound(ri, ci) or grid[ri][ci] == 0:
                return 1 
            if grid[ri][ci] == -1:
                return 0  

            grid[ri][ci] = -1  
            perimeter = 0

            for dx, dy in directions:
                perimeter += dfs(ri + dx, ci + dy)

            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j) 
        