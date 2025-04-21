class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        sumN, maxN, minN = 0, 0, 0
        for num in differences:
            sumN += num
            maxN = max(maxN, sumN)
            minN = min(minN, sumN)
        return max(0, upper - lower - maxN + minN + 1)