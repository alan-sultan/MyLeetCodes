class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            count = 1
            sumN = 0
            for weight in weights:
                if sumN + weight > mid:
                    count += 1
                    sumN = 0
                sumN += weight
                
            if count > days:
                low = mid + 1
            else:
                high = mid - 1
        return low
