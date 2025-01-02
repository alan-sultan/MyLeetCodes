class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        prv = 0
        prefix = [0] * (len(words) + 1)
        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prv += 1
            prefix[i + 1] = prv
        
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            l, r = q
            ans[i] = prefix[ r + 1] - prefix[l]

        return ans
            