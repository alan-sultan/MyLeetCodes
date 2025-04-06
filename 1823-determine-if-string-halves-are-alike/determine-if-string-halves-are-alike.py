class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("AEIOUaeiou")
        count = 0
        n = len(s)
        for i in range(n//2):
            count += s[i] in vowels
            count -= s[n - i - 1] in vowels
        return True if count == 0 else False