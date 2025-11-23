class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = []  
        for day in range(len(temperatures)):
            temp = temperatures[day]
            while stack and temperatures[stack[-1]] < temp:
                prevDay = stack.pop()  
                result[prevDay] = day - prevDay  
            stack.append(day)

        return result 