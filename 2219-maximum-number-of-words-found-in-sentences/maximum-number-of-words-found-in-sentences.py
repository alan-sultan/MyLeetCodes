class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxW = 0
        for sen in sentences:
            maxW = max(len(list(map(str, sen.split()))), maxW)
        return maxW
        