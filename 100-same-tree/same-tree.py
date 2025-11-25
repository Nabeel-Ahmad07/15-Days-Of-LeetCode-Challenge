# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def preorder(node, path):
            if not node:
                path.append(None)
                return
            path.append(node.val)
            preorder(node.left, path)
            preorder(node.right, path)
        
        pList, qList = [],[]
        preorder(p, pList)
        preorder(q, qList)

        if pList == qList:
            return True
        return False