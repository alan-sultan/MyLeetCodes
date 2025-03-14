class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        l, r = 1, max(candies)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            sumN = sum(num // mid for num in candies)
            if sumN >= k:
                ans = mid
                l = mid + 1
            else:
                r = mid -1
        return ans
