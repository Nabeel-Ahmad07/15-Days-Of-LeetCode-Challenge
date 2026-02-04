class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        firstList = nums[:n]
        secondList = nums[n:]

        newList = []

        for i in range(n):
            newList.append(firstList[i])
            newList.append(secondList[i])

        return newList