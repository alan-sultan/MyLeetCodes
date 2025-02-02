class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k:
            gifts.sort()
            gifts[-1] = int(sqrt(gifts[-1]))
            k -= 1
        return sum(gifts)