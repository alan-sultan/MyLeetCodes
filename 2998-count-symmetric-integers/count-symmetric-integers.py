class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0 
        while low <= high:
            if low < 100 and low % 11 == 0:
                ans += 1
            if 1000 <= low < 10000:
                fsum = low // 1000 + low % 1000 // 100
                lsum = low % 100 // 10 + low % 10
                if fsum == lsum:
                    ans += 1
            low += 1
        return ans