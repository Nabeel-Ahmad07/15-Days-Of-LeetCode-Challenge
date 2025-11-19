class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = nums[0]
        maxSum = nums[0]

        for num in nums[1:]:
            curr= max(num, curr+ num)  
            maxSum = max(maxSum, curr)
        return maxSum