class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles // numExchange > 0:
            d, r = divmod(numBottles, numExchange)
            ans += d
            numBottles = d + r
        return ans












