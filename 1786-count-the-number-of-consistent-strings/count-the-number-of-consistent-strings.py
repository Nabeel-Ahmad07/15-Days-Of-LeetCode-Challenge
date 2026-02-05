class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        alList = list(allowed)

        count = len(words)
        for word in words:
            
            for letter in word:
                if letter not in alList:
                    count -= 1
                    break
            else:
                continue
            continue


        return count