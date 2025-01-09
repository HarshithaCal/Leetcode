class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize minimum price and maximum profit
        min_buy_price = float('inf')
        max_profit = 0  

        for price in prices:
            # Update the minimum price so far
            min_buy_price = min(min_buy_price, price)

            # Calculate profit for the current price and update maximum profit
            max_profit = max(max_profit, price - min_buy_price)

        return max_profit

                

        






        