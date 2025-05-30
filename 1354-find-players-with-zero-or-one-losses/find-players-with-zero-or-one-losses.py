class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zeroL, oneL, moreL = set(), set(), set()

        for match in matches:
            w, l = match[0], match[1]
            if w not in oneL and w not in moreL:
                zeroL.add(w)
            if l in zeroL:
                zeroL.remove(l)
                oneL.add(l)
            elif l in oneL:
                oneL.remove(l)
                moreL.add(l)
            elif l in moreL:
                continue
            else:
                oneL.add(l)
        ans = [sorted(list(zeroL)), sorted(list(oneL))]
        return ans

