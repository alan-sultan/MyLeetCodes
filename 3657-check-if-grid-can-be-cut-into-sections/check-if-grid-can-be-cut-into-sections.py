class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(intervals):
            intervals.sort()
            
            sections = 0
            maxE = intervals[0][1]
            
            for start, end in intervals:
                if maxE <= start:
                    sections += 1
                maxE = max(maxE, end)
                
            return sections >= 2
        
        xI = [[rect[0], rect[2]] for rect in rectangles]
        yI = [[rect[1], rect[3]] for rect in rectangles]
        
        return check(xI) or check(yI)