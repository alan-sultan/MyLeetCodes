class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = blocks[:k].count('W')
        ans = count
        for i in range(len(blocks) - k):
            if blocks[i] == 'W':
                count -= 1
            if blocks[i + k] == 'W':
                count += 1
            ans = min(ans, count)
        return ans