class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        if n == 1: return prices
        for i in range(n):
            for j in range(i+1, n):
                if prices[j] <= prices[i]  and i<j:
                    prices[i] -= prices[j]
                    break

        return prices