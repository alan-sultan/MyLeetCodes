class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ct1 = ct2 = 1
        ans = [1]
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                ct1 += 1
            else:
                ct1 = 1

            if nums[i - 1] < nums[i]:
                ct2 += 1
            else:
                ct2 = 1
            ans.append(ct1)
            ans.append(ct2)
        return max(ans)
            
