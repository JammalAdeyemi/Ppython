# Two City Scheduling
# A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
# Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

# To solve the "Two City Scheduling" problem, where you need to minimize the total cost of flying `2n` people 
# to two cities (such that `n` people go to each city), a good approach is to first sort the candidates 
# based on the cost difference between flying to city A and city B. Then, send the first half of the 
# sorted list to the city that is cheaper for them, and the second half to the other city.

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        Calculate the minimum cost to fly every person to a city such that exactly n people arrive in each city.
        :type costs: List[List[int]]
        :rtype: int
        """
        # Sort the costs by the difference in cost between city A and city B
        costs.sort(key=lambda x: x[0] - x[1])
        total_cost = 0
        n = len(costs) // 2
        # Send the first half of people to city A and the second half to city B
        for i in range(n):
            total_cost += costs[i][0] + costs[i + n][1]
        return total_cost

### Explanation
# -Sort by Cost Difference: Sort the `costs` array based on the cost difference `aCosti - bCosti` for each
# person. This allows you to prioritize sending people to the city where they individually incur the least 
# additional cost.
# -Splitting the Group: The total number of people is `2n`, so `n` people should go to each city.
# -Calculating Total Cost:
  # -For the first `n` people (the first half of the sorted list), add their cost of going to city A 
  # (`costs[i][0]`).
  # -For the remaining `n` people (the second half of the sorted list), add their cost of going to city B
  # (`costs[i + n][1]`).
# -Returning the Result: The sum `total_cost` is the minimum cost to fly every person to a city such that 
# exactly `n` people arrive in each city.

### Time & Space Complexities
# -Time Complexity: O(n log n), where `n` is the number of people. The sorting of the array is the most 
# time-consuming part.
# -Space Complexity: O(1), as the solution does not use any additional space that scales with the size of 
# the input. The sorting is done in place, and only a few variables are used for calculations.
    