class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        queue = deque()
        ans = []

        for cou, prec in prerequisites:
            graph[prec].append(cou)
            inDegree[cou] += 1

        for cou in range(numCourses):
            if inDegree[cou] == 0:
                queue.append(cou)
            
        while queue:
            cou = queue.popleft()
            ans.append(cou)

            for neighbour in graph[cou]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)

        if len(ans) != numCourses:
            return []
        return ans
            