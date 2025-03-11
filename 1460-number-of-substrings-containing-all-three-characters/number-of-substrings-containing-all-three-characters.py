class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc = [-1, -1, -1]
        count, r = 0, 0
        while r < len(s):
            abc[ord(s[r]) - ord('a')] = r
            minI = min(abc)
            count += (minI + 1)
            r += 1
        return count