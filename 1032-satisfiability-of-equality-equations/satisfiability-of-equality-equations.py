class unionFind:
    def __init__(self):
        self.parent = [i for i in range(26)]
        self.size = [1] * 26
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
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uni = unionFind()
        for equation in equations:
            x = ord(equation[0]) - 97
            y = ord(equation[-1]) - 97
            if equation[1] == '=':
                uni.union(x, y)
        for equation in equations:
            x = ord(equation[0]) - 97
            y = ord(equation[-1]) - 97
            if equation[1] == '=':
                if uni.find(x) != uni.find(y):
                    return False
            else:
                if uni.find(x) == uni.find(y):
                    return False
        return True