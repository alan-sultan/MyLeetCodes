class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for ch in operations:
            if ch == "C":
                ans.pop()
            elif ch == "D":
                ans.append(2 * ans[-1])
            elif ch == "+":
                ans.append(ans[-1] + ans[-2])
            else:
                ans.append(int(ch))
        return sum(ans)