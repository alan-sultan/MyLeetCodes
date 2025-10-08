class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for num in spells:
            start = 0
            end = len(potions) - 1
            curr = 0
            while start <= end:
                mid = (start + end) // 2
                if potions[mid] * num >= success:
                    curr = len(potions) - mid
                    end = mid - 1
                else:
                    start = mid + 1
            ans.append(curr)
        return ans
