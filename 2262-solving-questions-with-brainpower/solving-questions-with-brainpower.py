class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[n-1] = questions[n-1][0]

        for i in range(n-2,-1,-1):
            pts,bp = questions[i]
            next_available_index = min(i + bp + 1 , n)
            Spts = pts + (dp[next_available_index] if next_available_index < n else 0)
            spts = dp[i+1]
            dp[i] = max(Spts , spts)

        return dp[0]