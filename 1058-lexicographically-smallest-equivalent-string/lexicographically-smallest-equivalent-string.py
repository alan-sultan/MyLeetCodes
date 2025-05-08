class unionFind:
    def __init__(self, n):
        self.parent = [i for i in range(26)]
        self.size = [1] * n
        self.minN = [i for i in range(26)]
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
                self.minN[parentX] = min(self.minN[parentX], self.minN[parentY])
            else:
                self.parent[parentX] = parentY
                self.size[parentY] += self.size[parentX]
                self.minN[parentY] = min(self.minN[parentX], self.minN[parentY])
    def minNode(self, x):
        parentX = self.find(x)
        return chr(self.minN[parentX] + 97)
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uni = unionFind(26)
        for i in range(len(s1)):
            x = ord(s1[i]) - 97
            y = ord(s2[i]) - 97
            uni.union(x, y)
        ans = ""
        for ch in baseStr:
            x = ord(ch) - 97
            ans += uni.minNode(x)
        return ans
