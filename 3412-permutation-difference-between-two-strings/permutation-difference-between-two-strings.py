class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        mp = {}
        for i in range(len(s)):
            mp[s[i]] = i

        return sum( abs(mp[t[i]] - i) for i in range(len(t)))
