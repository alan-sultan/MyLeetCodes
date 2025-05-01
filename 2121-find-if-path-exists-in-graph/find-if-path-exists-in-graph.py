class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = set()

        def dfs(node):
            if node == destination:
                return True

            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
            return False

        return dfs(source)