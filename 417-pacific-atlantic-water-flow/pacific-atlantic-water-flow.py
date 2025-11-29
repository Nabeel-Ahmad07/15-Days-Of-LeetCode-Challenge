class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(heights) 
        n = len(heights[0])
        def dfs(i, j, visited):
            visited.add((i,j))
            for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= x < m and 0 <= y < n and (x,y) not in visited and heights[x][y] >= heights[i][j]:
                    dfs(x, y, visited)
        pacific, atlantic = set(), set()
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m-1, j, atlantic)
        return list(pacific & atlantic)