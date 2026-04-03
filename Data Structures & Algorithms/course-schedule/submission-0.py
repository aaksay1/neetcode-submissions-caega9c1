class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = { i : [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)
        

        def dfs(path, node):
            if node in path:
                return False
            
            path.add(node)

            for nei in graph[node]:
                if dfs(path, nei) == False:
                    return False
            path.remove(node)

            return True
        for course in range(numCourses):
            if not dfs(set(), course):
                return False
        return True
