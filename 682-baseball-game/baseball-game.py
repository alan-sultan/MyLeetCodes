class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for i in range(len(operations)):
            if operations[i][0] == "-":
                x = 0 - int(operations[i][1:])
                ans.append(x)
            elif (operations[i]).isdigit():
                ans.append(int(operations[i]))
            elif operations[i] == "C":
                ans.pop()
            elif operations[i] == "D":
                ans.append(ans[-1] * 2)
            elif operations[i] == "+":
                x = ans[len(ans) - 1] + ans[len(ans) - 2]
                ans.append(x)
        return sum(ans)