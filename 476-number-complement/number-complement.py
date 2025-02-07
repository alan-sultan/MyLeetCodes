class Solution:
    def findComplement(self, num: int) -> int:
        x = format(num, 'b')
        y = str(int("1" * len(x)) - int(x))
        return int(y, 2)