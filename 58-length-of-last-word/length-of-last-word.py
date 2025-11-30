class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        rlist = list(s.split())
        return len(rlist[-1])
