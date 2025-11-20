class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortedStr = []
        anagrams = {}
        for s in strs:
            word = ''.join(sorted(s))
            sortedStr.append(word)

            if word not in anagrams:
                anagrams[word] = []
            anagrams[word].append(s)

            anagramsList = list(anagrams.values())
        return anagramsList




        