class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        curr = set()
        for x in arr:
            nextO = {x | y for y in curr}
            nextO.add(x)
            res.update(nextO)
            curr = nextO   
        return len(res)