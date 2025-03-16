class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 1
        r = cars * cars * min(ranks)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            count = 0
            for rank in ranks:
                count += int(sqrt(mid // rank))
            if count >= cars:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

      