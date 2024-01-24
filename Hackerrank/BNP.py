# Is Possible
# Consider a pair of integers, (a,b). The ffg operations can be performed on (a,b) in any order, zero or more times.
# * (a,b) - (a+b, b)
# * (a,b) - (a, a+b)
# Return a string that denotes whether or not (a,b) can be converted to (c,d) by performing the operation zero or more times.
# Example
# (a, b) = (1, 1)
# (c, d) = (5, 2)
# Perform the operation (1, 1 + 1) to (1,2), perform the operation (1 + 2, 2) to get (3,2), and perform the operation (3+2, 2)
# to get (5,2). Alternatively, the first operation could be (1+1, 1) to get (2,1), the second operation could be (2, 1+1) to get (2,2),
# and the third operation could be (2+2, 2) to get (4,2). The result is the same.
# Returns: str: "Yes" if (a, b) can be converted to (c, d) by performing zero or more of the operations described above. 
# Otherwise, returns "No".

def isPossible(a, b, c, d):
    # Write your code here
    while c >= a and d>=b:
        if (c==a and d>=b) or (d==b and c>=a):
            return "Yes"
        if c > d:
            c -= d
        else:
            d -= c
    return "No"


# This solution works by iteratively subtracting the smaller number from the larger one until either (c,d) equals (a,b) or (c,d) becomes smaller than (a,b). 
# The time complexity is usually approximately (c-a)+(d-b), but can be much larger when c and d are large and a and b are small. In worst case scenarios, the algorithm 
# performs poorly, so it's not suitable for large datasets. For those cases, the Extended Euclidean Algorithm for GCD would be a more efficient solution.



#  29. Predicting the Temperature
# Given the hourly temperature data for each 24 hour period in p prior days spanning from startDate to endDate inclusive, 
# predict the hourly temperature data for the next n days starting the first hour after endDate.
# Function Description
# Complete the function predictTemperature in the editor below. The function must return an array of floating-point numbers, 
# one predicted temperature for each hour of n days immediately following endDate in chronological order.
# predictTemperature has the following parameter(s):
# startDate: a string in the format yyyy-mm-dd endDate: a string in the format yyyy-mm-dd temperature[temperature[0],...temperature[(2 4*p)-1]]: an array floating-point numbers temperature[i] which represent the
# temperature at each yyyy-mm-dd hh:00 timestamp in the inclusive range from startDate to endDate.
# n: the integer number of days to predict
# Constraints
# • 2013-01-01 ≤ startDate < endDate ≤ 2015-01-01
# • 1 ≤ p ≤ 154
# • 1 ≤ n ≤ 48
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import numpy as np

def predictTemperature(startDate, endDate, temperature, n):
    # Step 1: Parse date strings to datetime objects
    start_date = datetime.strptime(startDate, '%Y-%m-%d')
    end_date = datetime.strptime(endDate, '%Y-%m-%d')

    # Step 2: Calculate time difference
    delta = (end_date - start_date).days

    # Step 3: Initialize an array to store predicted temperatures
    predicted_temperatures = []

    # Step 4: Create a linear regression model
    model = LinearRegression()

    # Prepare the data for regression
    X = np.arange(1, len(temperature) + 1).reshape(-1, 1)
    y = np.array(temperature)

    # Fit the model
    model.fit(X, y)

    # Predict temperatures for the next n days, one hour at a time
    for day in range(1, n + 1):
        for hour in range(24):
            # Calculate the hour offset from the start_date
            hour_offset = delta * 24 + day * 24 + hour

            # Use the model to predict the temperature for this hour
            predicted_temperature = model.predict(np.array([[hour_offset + 1]]))

            predicted_temperatures.append(predicted_temperature[0])

    return predicted_temperatures


