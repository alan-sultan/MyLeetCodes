class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        que = []
        for i, m in enumerate(mat):
            heapq.heappush(que, (m, i))
        ans = []
        for i in range(k):
            _, i = heapq.heappop(que)
            ans.append(i)
        return ans