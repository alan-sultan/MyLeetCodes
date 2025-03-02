class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle) 
        ans = 0
        for i in range(n):
            ans = ans * 26 + (ord(columnTitle[i]) - 64)
        return ans