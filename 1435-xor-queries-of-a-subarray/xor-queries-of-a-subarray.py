class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prf = [0]
        for i in range(len(arr)):
            prf.append(prf[i] ^ arr[i])
        ans = []
        for l, r in queries:
            ans.append(prf[l] ^ prf[r + 1])
        return ans