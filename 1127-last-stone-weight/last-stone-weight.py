class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        
        while True:
            if stones:
                x = heapq.heappop(stones)
            else:
                return 0
            if stones:
                y = heapq.heappop(stones)
                if x != y:
                    heapq.heappush(stones, -1 * abs(x - y))
            else:
                return -1 * x
