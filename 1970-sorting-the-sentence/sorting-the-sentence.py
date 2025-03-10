class Solution:
    def sortSentence(self, s: str) -> str:
        st = s.split()
        st = sorted(st, key=lambda x:x[-1])
        return ' '.join([st[:-1] for st in st])