class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        x = n // 2
        for i in range(-x, x + 1):
            if  n % 2 == 0 and i == 0:
                continue
            ans.append(i)
        return ans