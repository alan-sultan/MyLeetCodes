class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        ans = [[False] * numCourses for _ in range(numCourses)]
        for prec, cou in prerequisites:
            graph[prec].append(cou)

        for st in range(numCourses):
            seen = [False] * numCourses
            queue = deque([st])
            
            while queue:
                cou = queue.popleft()
                for neighbour in graph[cou]:
                    if not seen[neighbour]:
                        seen[neighbour] = True
                        ans[st][neighbour] = True
                        queue.append(neighbour)
        
        return [ans[pre][cou] for pre, cou in queries]

        # m=[[False]*numCourses for _ in range(numCourses)]
        
        # for u,v in prerequisites:
        #     m[u][v]=True
            
        # for k in range(numCourses):
        #     for i in range(numCourses):
        #         for j in range(numCourses):
        #             m[i][j]|=m[i][k] and m[k][j]
                    
        # ans=[]
        # for u,v in queries:
        #     ans.append(m[u][v])
            
        # return ans    