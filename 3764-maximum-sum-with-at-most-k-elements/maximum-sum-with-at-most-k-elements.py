class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        for i, row in enumerate(grid):
            row = sorted(row, reverse = True)
            for j in range(limits[i]):
                heappush(heap, -1 * (row[j]))
                
        sumN = 0
        for i in range(k):
            sumN += heappop(heap)
        return -1 * sumN
        