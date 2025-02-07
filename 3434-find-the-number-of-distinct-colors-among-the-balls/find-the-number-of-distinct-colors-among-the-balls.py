class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        xSet = {} 
        freq = defaultdict(int) 
        ans = []
        for x, y in queries:
            if x in xSet:
                oldY = xSet[x]
                freq[oldY] -= 1
                if freq[oldY] == 0:
                    del freq[oldY] 
            xSet[x] = y
            freq[y] += 1
            ans.append(len(freq))

        return ans

        

            