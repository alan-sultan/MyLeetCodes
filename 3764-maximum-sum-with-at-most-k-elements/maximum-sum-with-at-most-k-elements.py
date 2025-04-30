class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        ans = []
        for i, row in enumerate(grid):
            for ch in row:
                heappush(heap, -1 * (ch))
            for _ in range(limits[i]):
                heappush(ans, heappop(heap))
            while heap:
                heappop(heap)

        sumN = 0
        for i in range(k):
            sumN += heappop(ans)
        return -1 * sumN
        