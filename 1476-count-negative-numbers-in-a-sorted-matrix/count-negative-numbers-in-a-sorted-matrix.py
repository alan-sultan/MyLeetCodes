class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for layer in grid:
            n = len(layer)
            l, r = 0, n - 1
            while l <= r:
                if layer[l] < 0:
                    count += n - l
                    break
                elif layer[r] >= 0:
                    count += n - r - 1
                    break
                l += 1
                r -= 1
            else:
                count += n // 2
        return count