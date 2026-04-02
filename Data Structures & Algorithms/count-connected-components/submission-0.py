class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}

        res = 0

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        
        def dfs(node, visited):
            if node in visited:
                return True
            
            visited.add(node)

            for nei in graph[node]:
                dfs(nei, visited)

        for node in graph:
            if dfs(node, visited) == None:
                res += 1

        return res