class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        d, i = len(s), 0
        ans = []
        for ch in s:
            if ch == "I":
                ans.append(i)
                i += 1
            else:
                ans.append(d)
                d -= 1
        ans.append(i)
        return ans