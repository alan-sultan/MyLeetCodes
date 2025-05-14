class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        sD = s + s
        if len(s) != len(goal):
            return False
        return True if goal in sD else False