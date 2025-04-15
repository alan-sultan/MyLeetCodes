class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dic = {num: i for i, num in enumerate(nums1)}
        sortedI = []
        ans = 0
        for val in nums2:
            i = dic[val]
            leftC = bisect_left(sortedI, i)
            rightC = (len(nums1) - 1 - i) - (len(sortedI) - leftC)
            ans += leftC * rightC
            insort(sortedI, i)

        return ans
