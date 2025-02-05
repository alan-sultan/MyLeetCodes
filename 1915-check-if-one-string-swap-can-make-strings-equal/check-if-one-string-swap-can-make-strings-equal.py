class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c1, c2 = Counter(s1), Counter(s2)
        ans = 0
        if c1 != c2:
            return False
        for i in range(len(s2)):
            if s1[i] != s2[i]:  
                ans += 1
        return True if ans == 0 or ans == 2 else False
        

        