class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ct = ""
        for ch in s:
            ct += str(ord(ch) - 96) 
        SumN = 0
        print(ct)
        while k:
            sumN = sum(map(int, list(ct)))
            if sumN <= 9:
                break
            ct = str(sumN)
            k -= 1
        return sumN