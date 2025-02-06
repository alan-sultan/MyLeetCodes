class Solution:
    def splitNum(self, num: int) -> int:
        nums = sorted(str(num))
        x = y = ""
        for i in range(len(nums)):
            if i % 2:
                y += nums[i]
            else:
                x += nums[i]
        return int(x) + int(y)