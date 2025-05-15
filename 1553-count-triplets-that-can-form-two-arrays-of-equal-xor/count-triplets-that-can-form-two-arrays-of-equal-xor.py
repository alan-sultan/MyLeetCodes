class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prf = [0]
        n = len(arr)
        for i in range(n):
            prf.append(prf[i] ^ arr[i])
        count = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if prf[i] ^ prf[j + 1] == 0:
                    count += j - i
        return count