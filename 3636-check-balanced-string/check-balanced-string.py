class Solution:
    def isBalanced(self, num: str) -> bool:
        sumN = sum(map(int, num))
        oSum = 0
        for i in range(len(num)):
            if i % 2:
                oSum += int(num[i])
        return oSum * 2 == sumN

