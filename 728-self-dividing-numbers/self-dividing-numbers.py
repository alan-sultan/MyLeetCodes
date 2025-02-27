class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            for x in str(i):
                if x == '0' or i % int(x) != 0:
                    break
            else:
                ans.append(i)
        return ans