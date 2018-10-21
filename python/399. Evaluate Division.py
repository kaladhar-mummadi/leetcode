import collections


class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_util(self, source, target, visited):



        for i in self.graph[source]:
            if not visited[i]:
                visited[source] = True
                if self.dfs_util(i,target,visited):
                    return True
            elif source == target:

                return True
            else:

                return False

    def dfs(self, u, v):
        visited = [False] * (len(self.graph)+1)
        return self.dfs_util(u,v, visited)


class Solution:
    # def findRedundantConnection(self, edges):
    #     graph = Graph()
    #     for (u,v) in edges:
    #         graph.add_edge(u,v)
    #     for (u,v) in edges:
    #         temp = graph.dfs(u,v)
    #         print(u,v,temp)
    #         if temp:
    #             res = [u,v]
    #     return res

    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)



sol = Solution()
print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,3],[1,4],[1,5]]))