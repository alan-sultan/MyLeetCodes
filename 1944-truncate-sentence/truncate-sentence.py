class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        st = list(s.split())
        if len(st) < k:
            return s
        return " ".join(st[:k])