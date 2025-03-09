class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        for i in range(len(colors)):
            if i + 1 == len(colors):
                if colors[i - 1] != colors[i] != colors[0]:
                    count += 1
                continue
            if colors[i - 1] != colors[i] != colors[i + 1]:
                    count += 1
        return count