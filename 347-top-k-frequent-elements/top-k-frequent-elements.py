class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for key, val in count.items():
            heappush(heap, (-val, key))
        ans = []
        while k:
            _, v = heappop(heap)
            ans.append(v)
            k -= 1
        return ans