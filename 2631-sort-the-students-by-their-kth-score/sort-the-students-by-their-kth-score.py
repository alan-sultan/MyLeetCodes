class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # return sorted(score, key = lambda x: -x[k])
        grades = []
        dic = {}
        for student in score:
            grades.append(student[k])
            dic[student[k]] = student
        
        grades = sorted(grades, key = lambda x : -x)
        res = []

        for num in grades:
            res.append(dic[num])
        return res
        