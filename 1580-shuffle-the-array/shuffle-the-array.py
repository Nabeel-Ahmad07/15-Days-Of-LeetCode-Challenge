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
            for j in range(1):
                newList.append(firstList[i])
            for k in range(1):
                newList.append(secondList[i])

        return newList