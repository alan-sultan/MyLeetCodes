class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        def rec(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return 0
            if n % 2:
                memo[n] = 1 + rec(3 * n + 1)
            else:
                memo[n] = 1 + rec(n // 2)
            return memo[n]
        powers = [(i, rec(i)) for i in range(lo, hi + 1)]
        powers.sort(key = lambda x: (x[1], x[0]))
        return powers[k-1][0]