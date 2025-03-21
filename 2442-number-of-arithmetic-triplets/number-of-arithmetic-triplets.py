class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = {}
        count = 0
        for i in range(len(nums)):
            seen[nums[i]] = i
        for num in nums:
            if (num + diff) in seen and (num + 2 * diff) in seen:
                count += 1
        return count