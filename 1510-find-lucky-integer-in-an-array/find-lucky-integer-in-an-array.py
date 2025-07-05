class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = Counter(arr)
        ans = [-1]
        for key, val in dic.items():
            if key == val:
                ans.append(key)
        return max(ans)