class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            zeroC, oneC = 0, 0
            for j in range(i, n):
                if s[j] == '0':
                    zeroC += 1
                else:
                    oneC += 1
                
                if zeroC <= k or oneC <= k:
                    ans += 1

        return ans