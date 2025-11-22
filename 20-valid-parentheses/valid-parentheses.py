class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for elem in s:
            if elem in "({[":
                stack.append(elem)
            elif elem == "]":
                if not stack or stack.pop() != "[":
                    return False
            elif elem == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif elem == ")":
                if not stack or stack.pop() != "(":
                    return False
        return not stack
    
                