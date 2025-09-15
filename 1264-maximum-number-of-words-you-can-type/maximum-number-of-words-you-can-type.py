class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        mask = 0
        for ch in brokenLetters:
            mask |= 1 << (ord(ch) - 97)
        
        count = 0
        wordMask = 0
        n = len(text)
        for i in range(n + 1):
            if i < n and 'a' <= text[i] <= 'z':
                wordMask |= mask & (1 << (ord(text[i]) - 97))
            if i == n or text[i] == ' ':
                if wordMask == 0:
                    count += 1
                wordMask = 0
        return count