class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 1000000007

        n = len(s)
        freq = [0] * 26
        
        # Count frequency of each character
        for char in s:
            freq[ord(char) - ord('a')] += 1

        # Handle transformations in batches of 26
        while t >= 26:
            temp = [0] * 26
            for j in range(25):
                temp[j + 1] = (freq[j] + temp[j + 1]) % MOD
                temp[j] = (temp[j] + freq[j]) % MOD
            temp[25] = (temp[25] + freq[25]) % MOD
            temp[0] = (temp[0] + freq[25]) % MOD
            temp[1] = (temp[1] + freq[25]) % MOD
            freq = temp
            t -= 26

        ans = 0
        for i in range(26):
            diff = 26 - i
            if t >= diff:
                freq[i] = (2 * freq[i]) % MOD
            ans = (ans + freq[i]) % MOD

        return ans
