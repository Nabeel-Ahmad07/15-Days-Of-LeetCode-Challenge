class Solution(object):
   def twoSum(self, numbers, target, left=0, right=None):
        if right is None:
            right = len(numbers) - 1
    
        numberSum = numbers[left] + numbers[right]
        if numberSum == target:
            return [left + 1, right + 1] 
        if numberSum < target:
            return self.twoSum(numbers, target, left + 1, right) 
        return self.twoSum(numbers, target, left, right - 1)