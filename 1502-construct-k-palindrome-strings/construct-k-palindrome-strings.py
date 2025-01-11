class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        count = Counter(s)
        oddC = sum(freq % 2 for freq in count.values())
        return oddC <= k