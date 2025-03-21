class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        index = 0
        ii = 0
        for i in range(len(nums)):
            if nums[i] < target:
                index += 1
            elif nums[i] == target:
                ii += 1
        return [i for i in range(index, index + ii)]
