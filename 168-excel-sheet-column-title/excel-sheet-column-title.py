class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        stack = []
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, r = divmod(columnNumber, 26)
            stack.append(chr(r + 65))

        ans = ""
        while stack:
            ans += stack.pop()
        return ans