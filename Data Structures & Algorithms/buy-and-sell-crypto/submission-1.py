class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrices = [price for price in prices]
        maxProfit = 0
        for i in range(1, len(prices)):
            minPrices[i] = min(prices[i], minPrices[i - 1])
            maxProfit = max(maxProfit, prices[i] - minPrices[i - 1])

        return maxProfit