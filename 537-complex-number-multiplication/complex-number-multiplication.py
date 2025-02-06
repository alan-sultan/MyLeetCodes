class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, l1 = map(str,num1.split("+"))
        r2, l2 = map(str,num2.split("+"))
        x = int(r1) * int(r2) + (int(l1[:len(l1) - 1]) * int(l2[:len(l2) - 1])) * -1
        y = int(r1) * int(l2[:len(l2) - 1]) + int(r2) * int(l1[:len(l1) - 1])
        return f"{x}+{y}i"