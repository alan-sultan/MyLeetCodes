class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddC = 0
        for num in arr:
            if num % 2 == 1:
                oddC += 1
                if oddC == 3:
                    return True
            else:
                oddC = 0
        return False