class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        tot = 0
        for key, val in count.items():
            x = key + 1
            y = math.ceil(val / x)
            tot += y * x
        return tot