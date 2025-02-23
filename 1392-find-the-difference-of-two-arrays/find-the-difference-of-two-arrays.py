class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = set()
        for num in nums1:
            if num not in nums2:
                ans1.add(num)
        res = [list(ans1)]
        ans2 = set()
        for num in nums2:
            if num not in nums1:
                ans2.add(num)
        res.append(list(ans2))
        return res
        