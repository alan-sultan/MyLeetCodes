class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans = []
        # for i in range(n + 1):
        #     ans.append(i.bit_count())
        # return ans
        ans = [0]
        ls = 0
        for i in range(1, n + 1):
            if log2(i) == int(log2(i)):
                ans.append(1)
                ls = i
            else:
                print(ls, ans[ls])
                x = i - ls
                ans.append(ans[ls] + ans[x])
        return ans