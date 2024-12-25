class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxN = 0
        for acc in accounts:
            maxN = max(sum(acc), maxN)
        return maxN