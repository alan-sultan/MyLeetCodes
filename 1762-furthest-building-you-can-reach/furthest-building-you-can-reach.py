class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diff = []
        heapify(diff)
        for i in range(1, len(heights)):
            if heights[i - 1] < heights[i]:
                dif = heights[i] - heights[i - 1]
                heappush(diff, dif)
                if len(diff) > ladders:
                    bricks -= heappop(diff)
                if bricks < 0:
                    return i - 1
        return len(heights) - 1


            