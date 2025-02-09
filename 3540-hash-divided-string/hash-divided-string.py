class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = "" 
        for i in range(0, len(s), k):
            sumN = sum(ord(ch) - 97 for ch in s[i:i+k])
            x = sumN % 26
            res += chr(x + 97)
        return res