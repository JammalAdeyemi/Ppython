# Given the dataset of taxi rides completed in a pandas dataframe, process the dataframe as 
# follows:
# 1. drop all the rows where the pickup time/ dropoff time is missing
# 2. Find the longest ride(on basis of duration) for each pickup month(YYYY-MM).
# 3. sort the resulting dataframe by the pickup month
# the given dataframe consits of four coulmns:
# id - unique trip id
# vendor_id
# pickup_datetime
# dropoff_datetime

import pandas as pd
def longestRide(df):
    # Step 1: Drop rows with missing pickup or dropoff times
    df.dropna(subset=['pickup_datetime', 'dropoff_datetime'], inplace=True)

    # Step 2: Convert pickup and dropoff times to datetime objects
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])

    # Extract the pickup month (YYYY-MM) and calculate the ride duration
    df['pickup_month'] = df['pickup_datetime'].dt.strftime('%Y-%m')
    df['ride_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds()

    # Find the longest ride for each pickup month
    longest_rides = df.groupby('pickup_month')['ride_duration'].idxmax()
    longest_rides_df = df.loc[longest_rides]

    # Step 3: Select only the required columns
    result_df = longest_rides_df[['pickup_month', 'id']]

    return result_df

# Factors-of-3-and-5-
# Find the number of ideal integers within the given segment [low,high] inclusive. 
# An ideal number is a positive integer that has only 3 and 5 as prime divisors. An ideal 
# number can be expressed in the form of 3^x*5^y, where x and y are non-negativeintegers. 
# For example,15,45 and 75 are ideal numbers but 6,10,21 are not .Í
def getIdealNums(low, high):
    # Write your code here
    def countDivisors(num, divisor):
        count = 0
        while num % divisor == 0:
            num //= divisor
            count += 1
        return count
    ideal_count = 0
    for num in range(low, high + 1):
        count_3 = countDivisors(num, 3)
        count_5 = countDivisors(num, 5)
        
        if num == 3 ** count_3 * 5 ** count_5:
            ideal_count += 1
    return ideal_count

# Array Reduction 1 - Hackerrank
# there is an array of n integers called num. the array can be reduced by 1 element by 
# performing a move. each move consists of the ffg  3 steps:
# 1. Pick 2 diffierne elements num[i} and num[j], i is not eqaul to j.
# 2. Remove d 2 selected elements from the array
# 3. Add the sum of the 2 selected elements to the end of the array

# Each move has a cost associated with it: the sum of the 2 elements removed from the 
# array during the move. calculate the min total cost of reducing the array to one element.

import heapq
def reductionCost(num):
    # Write your code here
    if len(num) < 2:
        return 0
    
    heapq.heapify(num)
    total_cost = 0
    while len(num) > 1:
        smallest1 = heapq.heappop(num)
        smallest2 = heapq.heappop(num)
        
        move_cost = smallest1 + smallest2
        total_cost += move_cost
        
        heapq.heappush(num, move_cost)
    
    return total_cost

#Given the hourly temperature data for each  24hr period in p prior days spanning from 
# startDate to endDate inclusive, predict the hourl tempt data fro the next n days 
# starting the first hour after endDate
# FUNCTION DESC
# Complete the function predictTemperature  in the editor below. The function must return 
# an array of floating-point numbers, one predicted temperature for each hour of N  days 
# immediately following endDate  in chronological order. predictTemperature has the following parameter(s):
# startDate:  a string in the format yyyy-mm-dd
# endDate: a string in the format yyyy-mm-dd
# temperature[temperature[0],...temperature[(24*p)-1]]: an array floating-point numbers 
# temperature[i]  which represent the temperature at each yyyy-mm-dd hh:00  timestamp in the
# inclusive range from startDate to endDate.
# n: the int no of days to predict

from datetime import datetime, timedelta
def predictTemperature(startDate, endDate, temperature, n):
    # Write your code here
    start_date = datetime.strptime(startDate, '%Y-%m-%d')
    end_date = datetime.strptime(endDate, '%Y-%m-%d')
    
    total_hours = (end_date - start_date).total_seconds() / 3600 + 1
    complete_days = total_hours // 24
    remaining_hours = total_hours % 24
    if complete_days == 0:
        return temperature
        
    start_index = (complete_days * 24) % len(temperature)
    predicted_tempt = []
    average_tempt = [0] * 24
    for i in range(len(temperature)):
        hr = i % 24
        average_tempt[hr] += temperature[i]
    for i in range(24):
        average_tempt[i] /= complete_days
        
    for day in range(n):
        for hr in range(24):
            predicted_tempt.append(average_tempt[hr])
    return predicted_tempt[:int(n * 24)]