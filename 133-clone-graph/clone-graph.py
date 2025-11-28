"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        old = {}
        def dfs(n):
            if n in old: return old[n]
            copy = old[n] = Node(n.val)
            copy.neighbors = [dfs(x) for x in n.neighbors]
            return copy
        return dfs(node) if node else None