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
            return False
        else:
            return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uni = unionFind(len(edges))
        for u, v in edges:
            if uni.union(u - 1, v - 1):
                return [u, v]
            

        # def find(x):
        #     if p[x] != x:
        #         p[x] = find(p[x])
        #     return p[x]

        # p = list(range(1010))
        # for a, b in edges:
        #     if find(a) == find(b):
        #         return [a, b]
        #     p[find(a)] = find(b)
        # return []