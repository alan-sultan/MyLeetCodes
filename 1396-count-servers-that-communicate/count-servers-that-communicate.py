class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0

        for i in range(n):
            s = sum(grid[i])
            if s> 1:
                res += s
            elif s == 1:
                c = grid[i].index(1)
                if (sum(grid[i][c] for i in range(n))) > 1:
                    res += 1
        return res