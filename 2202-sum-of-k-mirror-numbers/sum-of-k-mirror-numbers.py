class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def generate():
            digits = 2

            for i in range(1, 10):
                yield i
            
            for i in range(1, 10):
                yield i * 11

            while True:
                for i in range(10**(digits-1), 10**digits):
                    yield int(str(i) + str(i)[::-1][1:])
                
                for i in range(10**(digits-1), 10**digits):
                    yield int(str(i) + str(i)[::-1])
                
                digits += 1
        
        def checkKPalindrome(num):
            baseKNum = ""
            while num > 0:
                baseKNum += str(num % k)
                num = num // k
            
            if baseKNum == baseKNum[::-1]:
                return True
            return False
        
        count = 0
        s = 0
        for i in generate():
            if checkKPalindrome(i):
                s += i
                count += 1

                if count == n:
                    break
        
        return s