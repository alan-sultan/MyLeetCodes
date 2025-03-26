class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vals = sorted([val for row in grid for val in row])
        
        diff = [abs(val - vals[0]) % x for val in vals]
        if any(d != 0 for d in diff):
            return -1
        
        median = vals[len(vals) // 2]
        operations = sum(abs(val - median) // x for val in vals)
        
        return operations