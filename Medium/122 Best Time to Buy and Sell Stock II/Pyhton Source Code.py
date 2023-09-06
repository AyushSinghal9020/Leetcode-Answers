class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:

        return_prices = []

        for val in prices:

            max_price = max(prices)

            prev_part = [
                max(prices) - prices[index]
                for index 
                in range(0 , prices.index(max_price))
            ]

            prices = prices.remove(max_price)

            return_prices.append(max(prev_part))

        return max(return_prices)
