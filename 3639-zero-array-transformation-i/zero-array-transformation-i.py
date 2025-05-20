class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        arr = [0] * (len(nums) + 1)
        for l, r in queries:
            arr[l] += 1
            arr[r + 1] -= 1
        operationCounts = []
        currentOperations = 0
        for delta in arr:
            currentOperations += delta
            operationCounts.append(currentOperations)
        for operations, target in zip(operationCounts, nums):
            if operations < target:
                return False
        return True