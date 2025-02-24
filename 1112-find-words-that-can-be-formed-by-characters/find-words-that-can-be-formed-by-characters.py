class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = defaultdict(int)
        for c in chars:
            counts[c] += 1
        
        ans = 0
        for word in words:
            word_count = defaultdict(int)
            for c in word:
                word_count[c] += 1
            
            for c, freq in word_count.items():
                if counts[c] < freq:
                    break
            else:
                ans += len(word)
            
        return ans