class Solution:
    def smallestNumber(self, n: int) -> int:
        tot = int(log2(1000))
        checker = [2 ** i for i in range(1, tot + 2)]
        idx = bisect_right(checker, n)
        return checker[idx] - 1