class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites: g[b].append(a)
        vis = [0]*numCourses
        def dfs(x):
            if vis[x] == 1: return False
            if vis[x] == 2: return True
            vis[x] = 1
            for y in g[x]:
                if not dfs(y): return False
            vis[x] = 2
            return True
        return all(dfs(i) for i in range(numCourses))