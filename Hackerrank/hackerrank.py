# A video player allows users to choose videos to play but it has some rules. The videos must be chosen in pairs and 
# each pair must have a duration which is a multiple of 60 seconds (e.g. 40 + 20, 90 + 30). Given the number of videos 
# and the list of video durations, calculate the total number of different video pairs that can be chosen. 
# Each video can only appear once in each pair, but can appear in multiple pairs. The order of videos in each pair is 
# not important.

# Complete the 'playlist' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY songs as parameter.
#

def playlist(songs):
    N = len(songs)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (songs[i] + songs[j]) % 60 == 0:
                count += 1
    return count

# DO THEY BELONG?
# A triangle formed by the three points a(x1, y1), b(x2, y2) and c(x3, y3) is a non-degenerate triangle if the 
# following rules are respected ( |ab| is the length of the line between a and b):
# |ab| + |bc| > |ac|
# |bc| + |ac| > |ab|
# |ab| + |ac| > |bc|
# A point to a triangle if it lies somewhere on or inside the triangle. Given two points p = (xp, yp)  and  q = (xq, yq),  return the correct scenario number:
# 0: If the triangle abc does not form a valid non-degenerate triangle.
# 1: if point p  belongs to the triangle but point q does not
# 2: if point q  belongs to the triangle but point p does not
# 3: if both point p & q belong to the triangle
# 3: If neither points doesn't belong
# Complete the 'pointsBelong' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#  5. INTEGER x3
#  6. INTEGER y3
#  7. INTEGER xp
#  8. INTEGER yp
#  9. INTEGER xq
#  10. INTEGER yq
#

import math

def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    def isInside(x, y, x1, y1, x2, y2, x3, y3):
        A = ((x2 - x1)*(y - y1) - (y2 - y1)*(x - x1)) 
        B = ((x3 - x2)*(y - y2) - (y3 - y2)*(x - x2))
        C = ((x1 - x3)*(y - y3) - (y1 - y3)*(x - x3))
        return (A >= 0 and B >= 0 and C >= 0) or (A <= 0 and B <= 0 and C <= 0)
    
    ab = math.sqrt((x1 - x2)**2 + (y1 - y2)**2) 
    bc = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    ac = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    
    if ab + bc <= ac or bc + ac <= ab or ab + ac <= bc:
        return 0
    
    if isInside(xp, yp, x1, y1, x2, y2, x3, y3):
        if isInside(xq, yq, x1, y1, x2, y2, x3, y3):
            return 3
        else:
            return 1
            
    elif isInside(xq, yq, x1, y1, x2, y2, x3, y3):
        return 2
    else:
        return 4



def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    # Check if abc forms a valid triangle
    ab = math.sqrt((x1 - x2)**2 + (y1 - y2)**2) 
    bc = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    ac = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    
    if ab + bc <= ac or bc + ac <= ab or ab + ac <= bc:
        return 0
    
    # Check if p is inside triangle
    if isInside(xp, yp, x1, y1, x2, y2, x3, y3):
        if isInside(xq, yq, x1, y1, x2, y2, x3, y3):
            return 3
        else:
            return 1
            
    # Check if q is inside triangle            
    elif isInside(xq, yq, x1, y1, x2, y2, x3, y3):
        return 2

    else:
        return 4
        
def isInside(x, y, x1, y1, x2, y2, x3, y3):
    A = ((x2 - x1)*(y - y1) - (y2 - y1)*(x - x1)) 
    B = ((x3 - x2)*(y - y2) - (y3 - y2)*(x - x2))
    C = ((x1 - x3)*(y - y3) - (y1 - y3)*(x - x3))
    return (A >= 0 and B >= 0 and C >= 0) or (A <= 0 and B <= 0 and C <= 0)


# CHAIRS REQUIREMENT
# In this challenge, determine the minimum number of chairs to be purchased to accommodate all workers in a new business 
# workroom. There is no chair at the beginning. There will be a string array of simulations. each simulation is described by 
# a combination of 4 characters: C,R,U,L. 
# C: a new EMPLOYEE ARRIVES in the workroom, if there is a chair available, the employee takes it. otherwise, 
# a new chair is purchased.
# R: an employee goes to a meeting room, freeing up their chair.
# U: an employee arrives from a meeting room. if there is a chair available, the employee takes it. otherwise, a new
# chair is purchased.
# L: an employee leaves the workroom, freeing up their chair.
# Constraints:
# 1 <= n <= 100
# 1 <= length of each simulation[i] <= 10000
# Complete the 'minChairs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY simulations as parameter.
#


def minChairs(simulations):
    results = []
    for simulation in simulations:
        chairs = 0
        free_chairs = 0
        for action in simulation:
            if action == 'C':
                if free_chairs > 0:
                    free_chairs -= 1
                else:
                    chairs += 1
            elif action == 'R' or action == 'L':
                free_chairs += 1
            elif action == 'U':
                if free_chairs > 0:
                    free_chairs -= 1
                else:
                    chairs += 1
        results.append(chairs)
    return results




# THRESHOLD ALERTS
# A compliance system monitors incoming and outbound calls. It sends an alert whenerver the avg number of calls over
# a trailing number of mins exceeds a threshold. If the number of trailing mins to cconsider, precedingMinutes = 5, 
# at time T, take the average the call vols for times T - (5-1), T-(5-2)....T-(5-5).

# CONSTRAINTS
# * 1<=precedingMinutes<=n
# * 1<=alertThreshold<=10**5
# * 1<= n <=10**5
# * 0 <=numCalls[i]<=10**5
    
def numberOfAlerts(precedingMinutes, alertThreshold, numCalls):
    # Write your code here
    total_alerts = 0
    trailing_sum = sum(numCalls[:precedingMinutes])
    
    for i in range(precedingMinutes, len(numCalls)):
        avg_calls = trailing_sum / precedingMinutes
        if avg_calls > alertThreshold:
            total_alerts += 1
        
        trailing_sum -= numCalls[i - precedingMinutes]
        trailing_sum += numCalls[i]
    
    # Check for the last set of trailing minutes
    avg_calls = trailing_sum / precedingMinutes
    if avg_calls > alertThreshold:
        total_alerts += 1
    
    return total_alerts


# PREPROCESS DATES
# On a web form, users are asked to enter dates which come in as strings. Before storing them to the database, 
# they need to be converted to a standard date format. Write a function to convert the dates as described. 
# Given a date string in the format DAY MONTH YEAR, where:

# * DAY a string in the form "1st","2nd" and all others are the number + "th" / "st"
# * MONTH is the first 3 letters of the english language months like "Jan", "Dec" etc
# * YEAR is 4 digits ranging from 1900 to 2100.

# Convert the date string "DAY MONTH YEAR" to the date string "YYYY-MM-DD" in the format 
# "4 digit year - 2 digit month - 2 digit day".
 from datetime import datetime
def preprocessDate(dates):
    
    def get_month_number(month):
        months = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        return months[month]
    
    processed_dates = []
    for date in dates:
        day, month, year = date.split()
        day = day[:-2] if day[-2:] in ("st", "nd", "rd", "th") else day
        month = get_month_number(month)
        formatted_date = f"{year}-{month}-{day.zfill(2)}"
        processed_dates.append(formatted_date)
    
    return processed_dates
    

# 1. Random walk card game
# Consider the following game. Beginning with a deck of even size = N cards that are half 
# red and half green (N/2 each), you begin drawing cards. For each red card, you win $1 and 
# for each green card you lose $1. You may stop at any time. What is the value of this game
# to you assuming you play optimally? Write a program that computes this value. Note that it
# will be tested against large values of N.

def game_value(deck_size):
    counts = [0] * (deck_size + 1)
    
    for red in range(1, deck_size // 2 + 1):
        for green in range(red):
            remaining = deck_size - red - green
            prob_red = (deck_size / 2 - red) / (remaining - 1)
            prob_green = (deck_size / 2 - green) / (remaining - 1)
            
            value_red = 0
            if red - 1 + green >= 0 and red - 1 + green <= deck_size:
                value_red = 1 + counts[red - 1 + green]
            
            value_green = 0
            if red + green >= 0 and red + green <= deck_size:
                value_green = -1 + counts[red + green]
            
            counts[red + green] = max(0, prob_red * value_red + prob_green * value_green)
    
    return round(counts[deck_size // 2], 2)


    
    