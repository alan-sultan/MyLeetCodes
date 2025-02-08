class Solution:
    def sortVowels(self, s: str) -> str:
        vow = []
        for ch in s:
            if ch in "aeiouAEIOU":
                vow += ch
        vow.sort()
        j = 0
        res = ""
        for i, ch in enumerate(s):
            if ch in "aeiouAEIOU":
                res += vow[j]
                j += 1
            else:
                res += ch
        return res
