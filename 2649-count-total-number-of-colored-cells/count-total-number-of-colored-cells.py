class Solution:
    def coloredCells(self, n: int) -> int:
        # 1 4 8 12 16 
        if n == 1:
            return n
        else:
            return ((n - 1) * n * 2) + 1