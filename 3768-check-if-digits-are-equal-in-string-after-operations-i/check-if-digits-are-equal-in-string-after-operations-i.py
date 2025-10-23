class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            x = ""
            for i in range(1, len(s)):
                x += str((int(s[i - 1])+ int(s[i])) % 10)
            s = x
        return s[0] == s[1]