class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        count = nums.count(0)

        if count > 1:
            return [0] * len(nums)

        for num in nums:
            if num != 0:
                product *= num

        result = []
        for num in nums:
            if count == 0:
                result.append(product // num)
            else:
                result.append(product if num == 0 else 0)

        return result