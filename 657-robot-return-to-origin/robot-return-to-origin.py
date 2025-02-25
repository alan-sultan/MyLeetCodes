class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ud = lr = 0
        for ch in moves:
            if ch == 'U':
                ud += 1
            elif ch == 'D':
                ud -= 1
            elif ch == 'L':
                lr -= 1
            else:
                lr += 1
        if lr == 0 and ud == 0:
            return True
        return False