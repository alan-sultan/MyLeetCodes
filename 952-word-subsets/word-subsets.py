class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        from collections import Counter

        count = Counter()
        for word in words2:
            count |= Counter(word)

        res = []
        for word in words1:
            freq = Counter(word)
            if all(freq[char] >= count[char] for char in count):
                res.append(word)

        return res