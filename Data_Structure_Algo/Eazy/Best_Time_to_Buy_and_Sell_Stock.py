## Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize 
# your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that 
# stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Thought Process and Concepts Utilized
# 1. Problem Understanding:
# • The goal is to find the maximum profit from a single buy and sell transaction given a list of stock prices, where each element represents the stock's price on that day.
# • The buy must occur before the sell.
# • If no profit is possible, the function should return 0.

# 2. Algorithm Choice:
# • Single Pass Approach: A single traversal of the price array is sufficient to find the maximum profit. The key is to track the minimum buying price and the maximum profit at each step.
# • Greedy Method: This problem is approached using a greedy algorithm, where the optimal solution at each step (minimum purchase price and maximum selling price following it) contributes to the global optimum.

# 3. Implementation Details:
# • Tracking Minimum Price: Initialize a variable min_price to a very high value. Update min_price whenever a lower price is encountered in the array.
# • Calculating Maximum Profit: Initialize max_profit to 0. For each price, calculate the profit if bought at min_price and sold at the current price. Update max_profit if this profit is greater than the current max_profit.
# • Return Value: The value of max_profit after traversing the entire array is the maximum profit achievable. If no profit is possible, it remains 0.

# 4. Time & Space Complexities:
# • Time Complexity: O(n), where n is the number of days/prices in the array. The array is traversed once, and each operation within the loop is O(1).
# • Space Complexity: O(1), as the solution uses only a fixed number of variables (min_price and max_profit) regardless of the input size.

class Solution(object):
    def maxProfit(self, prices):
        """
        Find the maximum profit that can be achieved from a single buy and sell transaction.
        :type prices: List[int]
        :rtype: int
        """
        # Initialize variables to keep track of the minimum price and maximum profit
        min_price, max_profit = float('inf'), 0
        for price in prices: # Iterate over each price
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate the profit if the stock were sold today
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

## Explanation
# • Initialization: We initialize min_price to an infinitely large value and max_profit to 0. min_price will keep track of the lowest price encountered so far, and max_profit will store the highest profit that can be made.
# • Iterating through Prices: We iterate through each price in the prices array.
    # • If the current price is less than min_price, we update min_price.
    # • If the current price minus min_price (the profit if bought at min_price and sold today) is greater than max_profit, we update max_profit.
# • Result: The value of max_profit at the end of the iteration is the maximum profit that can be achieved.