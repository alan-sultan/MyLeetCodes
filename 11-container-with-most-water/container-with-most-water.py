class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        maxA = 0
        while(l < r):
            if(height[l] < height[r]):
                curA = (r - l) * height[l]
                maxA = max(maxA, curA)
                l += 1
            else:
                curA = (r - l) * height[r]
                maxA = max(maxA, curA)
                r -= 1
        return maxA
