class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        hp = [(num, i) for i, num in enumerate(nums)]
        heapify(hp)
        for _ in range(k):
            _, i = heappop(hp)
            nums[i] *= multiplier
            heappush(hp, (nums[i], i))
        return nums