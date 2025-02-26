class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minPsum = 0
        maxPsum = 0
        Psum = 0

        for num in nums:
            Psum += num

            minPsum = min(minPsum, Psum)
            maxPsum = max(maxPsum, Psum)

        return maxPsum - minPsum