class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = {}
        count = 0
        for dominoe in dominoes:
            if (k := (min(dominoe), max(dominoe))) in dic:
                count += dic[k]
                dic[k] += 1
            else:
                dic[k] = 1
        return count
        