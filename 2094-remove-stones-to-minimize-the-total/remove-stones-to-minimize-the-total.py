class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        i = 0
        nums = [-1 * num for num in piles]
        heapq.heapify(nums)
        while i < k:
            num = heapq.heappop(nums)
            heapq.heappush(nums, num  + ((-1 * num) // 2))
            i += 1
        return sum(nums) * -1
