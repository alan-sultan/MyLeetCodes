class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            num = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, num)
            count += 1
        return count
