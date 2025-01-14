class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x == 100:
            return 1
        else:
            y = (x % 10) + (x // 10)
            return y if x % y == 0 else -1
