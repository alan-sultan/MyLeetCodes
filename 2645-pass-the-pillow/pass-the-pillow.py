class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        isf = True
        while time:
            if i == n:
                isf = False
            if i == 1:
                isf = True
            if isf:
                i += 1
                time -= 1
            else:
                i -= 1
                time -= 1
        return i
            