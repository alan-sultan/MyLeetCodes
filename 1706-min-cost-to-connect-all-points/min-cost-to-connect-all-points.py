class unionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            if self.size[parentX] > self.size[parentY]:
                self.parent[parentY] = parentX
                self.size[parentX] += self.size[parentY]
            else:
                self.parent[parentX] = parentY
                self.size[parentY] += self.size[parentX]
            return True
        return False
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uni = unionFind(len(points))
        edges = []
        for i, pts in enumerate(points):
            u, v = pts
            for j in range(i + 1, len(points)):
                u1, v1 = points[j]
                cost = abs(u - u1) + abs(v - v1)
                heappush(edges, (cost, i, j))
        ans = 0
        while edges:
            cost, u, v = heappop(edges)
            if uni.union(u, v):
                ans += cost
        return ans

