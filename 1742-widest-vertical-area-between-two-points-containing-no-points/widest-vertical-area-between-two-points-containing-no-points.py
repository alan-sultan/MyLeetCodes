class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xS = sorted([x for x, _ in points])
        return max(xS[i] - xS[i - 1] for i in range(1, len(xS)))