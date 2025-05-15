class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        che = []
        for s, e in ranges:
            for i in range(s, e + 1):
                che.append(i)
        for i in range(left, right + 1):
            if i not in che:
                return False
        return True
