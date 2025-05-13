class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z =  x ^ y
        count = 0
        while z > 0:
            if z & 1 == 1:
                count += 1
            z >>= 1
        return count