class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        minN = float('inf')
        r1sum = sum(grid[0])
        r2sum = 0
        
        for i in range(len(grid[0])):
            r1sum -= grid[0][i]
            minN = min(minN, max(r1sum, r2sum))
            r2sum += grid[1][i]
        return minN