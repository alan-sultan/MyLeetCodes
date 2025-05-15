class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        xorDic = {0 : -1}
        eve = {'a': 1, 'e' : 2, 'i' : 4, 'o' : 8, 'u' : 16}
        runXor = 0
        maxLen = 0
        for i, ch in enumerate(s):
            if ch in eve:
                runXor ^= eve[ch]
            if runXor in xorDic:
                maxLen = max(maxLen, i - xorDic[runXor])
            else:
                xorDic[runXor] = i
        return maxLen