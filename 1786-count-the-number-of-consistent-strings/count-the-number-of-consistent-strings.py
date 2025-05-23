class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            for chr in word:
                if chr not in allowed:
                    count += 1
                    break
        return len(words) - count