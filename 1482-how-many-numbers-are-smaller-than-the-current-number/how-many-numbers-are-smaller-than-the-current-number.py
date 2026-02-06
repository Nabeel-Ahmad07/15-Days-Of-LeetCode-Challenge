class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        count = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            out.append(count)
            count = 0

        return out  
        