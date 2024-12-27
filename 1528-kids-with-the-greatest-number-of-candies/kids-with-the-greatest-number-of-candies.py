class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if candie + extraCandies >= max(candies) else False for candie in candies]
        
        
