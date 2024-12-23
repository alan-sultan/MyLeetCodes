class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sumN = n * (n + 1) // 2
        t = n // m
        m_s = m * t * (t + 1) // 2
        return sumN - 2 * m_s