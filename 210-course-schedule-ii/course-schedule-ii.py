class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        heap = []
        ans = []

        for cou, prec in prerequisites:
            graph[prec].append(cou)
            inDegree[cou] += 1

        for cou in range(numCourses):
            if inDegree[cou] == 0:
                heappush(heap, cou)
            
        while heap:
            cou = heappop(heap)
            ans.append(cou)

            for neighbour in graph[cou]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    heappush(heap, neighbour)

        if len(ans) != numCourses:
            return []
        return ans
            