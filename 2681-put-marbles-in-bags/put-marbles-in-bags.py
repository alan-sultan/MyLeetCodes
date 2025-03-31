class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairW = [weights[i] + weights[i + 1] for i in range(n - 1)]
        pairW.sort()
        
        ans = 0
        for i in range(k - 1):
            ans += pairW[n - 2 - i] - pairW[i]
        return ans