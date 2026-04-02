class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = {i : [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)  

        def dfs(curr, parent, visited):
            
            if curr in visited:
                return False
            
            visited.add(curr)
            for nei in graph[curr]:
                if nei in visited and nei != parent:
                    return False
                
                if nei not in visited:
                    if not dfs(nei, curr, visited):  
                        return False
            return True
        
        visited = set()

        if not dfs(0, -1, visited):
            return False

        return len(visited) == n

