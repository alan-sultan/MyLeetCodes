class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        c = s.count('1') - 1
        return "1" * c + "0" * (n - c - 1) + "1"