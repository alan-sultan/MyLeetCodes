class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n > 0:
            d, r = divmod(n, k)
            res += r
            n = d
        return res