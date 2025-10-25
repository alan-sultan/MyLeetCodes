class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        money = w * 28
        money += (7 * w *( w - 1)) // 2

        if (n % 7):
            extradD = n % 7
            moneyA = w + 1
            for i in range(extradD):
                money += moneyA
                moneyA += 1
        return money