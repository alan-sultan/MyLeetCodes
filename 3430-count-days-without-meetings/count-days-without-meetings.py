class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        freeD = 0
        latesE = 0
        meetings.sort()

        for start, end in meetings:
            if start > latesE + 1:
                freeD += start - latesE - 1
            latesE = max(latesE, end)
        freeD += days - latesE

        return freeD