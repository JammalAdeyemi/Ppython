## Best Time to Buy and Sell Stock 2
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day. On each day, 
# you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

### Thought Process and Concepts Utilized
# 1. Problem Understanding:
# - The task is to maximize profit from buying and selling stock given daily prices.
# - Multiple transactions are allowed, but only one share of the stock can be held at a time.
# - Transactions can occur on the same day, meaning one can buy and then sell immediately.

# 2. Algorithm Choice:
# - Greedy Approach: This problem is approached with a greedy algorithm that captures the profit whenever possible
# without looking ahead for more significant benefits. This works because the gain from each transaction is 
# independent.
# - Local Optima to Global Optima: By summing all positive price differences (local optima), we ensure that we 
# reach the global optimum of maximum profit.

# 3. Implementation Details:
# - Profit Accumulation: Initialize `max_profit` to 0. Iterate through the price list, and when a price increase 
# is detected compared to the previous day, add the difference to `max_profit`.
# - Consecutive Day Comparison: Start from the second day and compare with the previous day. If the price on the 
# current day is higher, it's a potential transaction day.
# - Transaction Rule: Apply the rule that each increase in price represents a buying and immediate selling 
# opportunity, and accumulate the profit.

class Solution(object):
    def maxProfit(self, prices):
        """
        Calculate the maximum profit from multiple transactions.
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        # Loop through the array of prices
        for i in range(1, len(prices)):
            # If selling on day i is profitable, add the profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]      
        return max_profit

### Explanation
# - We initialize `max_profit` to 0.
# - We iterate through the list of prices from the second day (`i = 1`) to the end.
# - For each day, if the price is higher than the previous day, we consider it as a profitable transaction. 
# We sell the stock bought the previous day and buy it again if the price is still increasing.
# - We add the profit from each transaction to `max_profit`.
# - Finally, we return the `max_profit` after going through all the days.

### Time & Space Complexities
# - Time Complexity: O(n), where `n` is the number of days in the `prices` array. We go through all the days once 
# to calculate the profit.
# - Space Complexity: O(1), as we only use a single additional variable `max_profit` to keep track of our running 
# total profit, irrespective of the number of prices given.

### Summary
# The solution is grounded in the understanding that capturing every small profit leads to the maximum possible 
# profit. This insight simplifies the problem to a series of local decisions without the need for complex state 
# maintenance or lookahead strategies. By iterating through the list once and constantly accumulating profitable 
# transactions, we effectively reach the optimal solution. The greedy algorithm is particularly well-suited for 
# this problem because the future stock prices do not affect the decision to make a profit today.

print(list(range(4,10,2)))