class Solution:
    def minPartitions(self, n: str) -> int:
        for num in range(9, -1, -1):
            if str(num) in n:
                return num
