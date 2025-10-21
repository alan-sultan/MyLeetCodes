class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(Counter(word).values())
        if len(count) == 1:
            return 1 in count or 1 in count.values()
        if len(count) == 2:
            return count[1] == 1 or count[min(count) + 1] == 1
        return False