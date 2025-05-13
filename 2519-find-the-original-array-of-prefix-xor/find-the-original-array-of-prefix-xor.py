class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        for i, num in enumerate(pref):
            if i == 0:
                continue
            ans.append(pref[i] ^ pref[i - 1])
        return ans
            
        
