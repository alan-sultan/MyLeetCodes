class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        for i in range(len(nums2)):
            nums2[i] = nums2[i] * k
        
        return sum(num1 % num2 == 0 for num1 in nums1 for num2 in nums2)