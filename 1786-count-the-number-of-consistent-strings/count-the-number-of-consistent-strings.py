class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            if all(ch in set(allowed) for ch in set(word)):
                count += 1
        return count