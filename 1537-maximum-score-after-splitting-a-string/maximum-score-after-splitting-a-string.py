class Solution:
    def maxScore(self, s: str) -> int:
        prefix = sum(map(int, s))
        maxN = 0
        countZ = 0
        for i in range(len(s) - 1):
            if s[i] =='0':
                countZ += 1
            else:
                prefix -= 1
            maxN = max(maxN, prefix + countZ)
            
        return maxN