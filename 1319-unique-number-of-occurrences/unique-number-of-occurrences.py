class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        ans = count.values()
        return True if len(ans) == len(set(ans)) else False