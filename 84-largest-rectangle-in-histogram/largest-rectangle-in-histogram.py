class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [] 
        maximumArea = 0
        heights.append(0) 
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maximumArea = max(maximumArea, height * width)
            stack.append(i)
        return maximumArea