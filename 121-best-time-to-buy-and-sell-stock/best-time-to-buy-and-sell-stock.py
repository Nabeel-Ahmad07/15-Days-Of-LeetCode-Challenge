class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = float('inf')
        high = 0

        for i in range(len(prices)):
            if prices[i]<low:
                low = prices[i]
            else:
                profit = prices[i]-low
                high = max(high, profit)
        return high
