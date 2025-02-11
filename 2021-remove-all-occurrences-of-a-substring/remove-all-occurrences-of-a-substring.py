class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while(part in s):
            x = s.index(part)
            s = s[:x] + s[x + len(part):]
        return s 