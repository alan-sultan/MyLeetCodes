class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count,count1=0,0
        for x in nums1:
            if x in nums2:
                count+=1
        for x in nums2:
            if x in nums1:
                count1+=1
        return count,count1