class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        index = {}   
        left = 0         
        maxLen = 0

        for right in range(len(s)):
            char = s[right]
            if char in index and index[char] >= left:
                left = index[char] + 1 

            index[char] = right
            maxLen = max(maxLen, right - left + 1)
        return maxLen