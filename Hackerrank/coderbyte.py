# Have the function ArrayChallenge(arr) take the array of numbers stored in arr which will contain 
# integers that represent the amount in dollars that a single stock is worth, and return the maximum profit 
# that could have been made by buying stock on day x and selling stock on day y where y > x. 
# For example: if arr is [44, 30, 24, 32, 35, 30, 40, 38, 15] then your program should return 16 
# because at index 2 the stock was worth $24 and at index 6 the stock was then worth $40, so if you 
# bought the stock at 24 and sold it at 40, you would have made a profit of $16, which is the maximum profit 
# that could have been made with this list of stock prices.If there is not profit that could have been made 
# with the stock prices, then your program should return -1. For example: arr is [10, 9, 8, 2] then your 
# program should return -1.

def ArrayChallenge(arr):
    max_profit = -1
    min_price = arr[0]
    
    for price in arr:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
                
    return max_profit

# Have the function ArrayChallenge(arr) read the input array of 4 numbers x, y, a, b, separated by space,
# and return an output of two numbers for updated a and b (assume the learning rate is 1). Save up to 3 
# digits after the decimal points for a and b. The output should be a string in the format: a, b

# Logistic regression is a simple approach to do classification, and the same formula is also commonly 
# used as the output layer in neural networks. We assume both the input and output variables are scalars,
# and the logistic regression can be written as: y = 1.0 / (1.0 + exp(-ax - b))

# After observing a data example (x, y), the parameter a and b can be updated using gradient descent 
# with a learning rate.
import math
def ArrayChallenge(arr):
    x, y, a, b = arr
    y_hat = 1 / (1 + math.exp(-a * x - b))
    a += (y - y_hat) * x
    b += y - y_hat
    return '{:.3f}, {:.3f}'.format(a, b)

arr = np.array([2.2, 0.0, 5.1, 5.7])
arr2 = np.array([1.0, 1.0, 1.0,1.0])

import numpy as np
def ArrayChallenge(arr):

  # code goes here
  learnrate = 1
  x = arr[0]
  y = arr[1]
  a = arr[2]
  b = arr[3]
  y_pred = 1 / (1 + np.exp(np.dot(x, -a) - b))
  error = y - y_pred
  a_new = a - learnrate * error * x
  b_new = b - learnrate * error
  return "{:.3f}, {:.3f}".format(a_new, b_new).rstrip('0').rstrip('.')

# Have the function StringChallenge(strArr) take the strArr parameter being passed, which will only 
# contain a single element, and return the string true if it is a valid number that contains only digits
# with properly placed decimals and commas, otherwise return the string false. For example: if strArr is
# ["1,093,222.04"] then your program should return the string true, but if the input were ["1,093,22.04"]
# then your program should return the string false. The input may contain characters other than digits.
def StringChallenge(strArr):
    num_str = strArr[0]
    decimal_count = 0
    comma_count = 0

    # check each character in the string
    for c in num_str:
        if c.isdigit():
            continue
        elif c == '.':
            decimal_count += 1
            if decimal_count > 1 or comma_count > 0:
                return "false"
        elif c == ',':
            comma_count += 1
            if comma_count > 2 or decimal_count > 0:
                return "false"
        else:
            return "false"

    # there should be at least one digit before any comma or decimal point
    if comma_count > 0 and not num_str.replace(',', '').isdigit():
        return "false"
    if decimal_count > 0 and not num_str.replace('.', '').isdigit():
        return "false"

    # the number is valid
    return "true"


# Have the function MathChallenge(strArr) take strArr which will be an array of 4 coordinates in the 
# form: (x,y). Your program should take these points where the first 2 form a line and the last 2 form a line, 
# and determine whether the lines intersect, and if they do, at what point. For example: if strArr is 
# ["(3,0)","(1,4)","(0,-3)","(2,3)"], then the line created by (3,0) and (1,4) and the line created by (0,-3) (2,3) 
# intersect at (9/5,12/5). Your output should therefore be the 2 points in fraction form in the following 
# format: (9/5,12/5). If there is no denominator for the resulting points, then the output should just be the integers 
# like so: (12,3). If any of the resulting points is negative, add the negative sign to the numerator like so: 
# (-491/63,-491/67). If there is no intersection, your output should return the string "no intersection". The input points 
# and the resulting points can be positive or negative integers.
def MathChallenge(strArr):
    # parse the input coordinates
    coord1 = parse_coord(strArr[0])
    coord2 = parse_coord(strArr[1])
    coord3 = parse_coord(strArr[2])
    coord4 = parse_coord(strArr[3])

    # compute the slopes and y-intercepts of the two lines
    m1 = slope(coord1, coord2)
    b1 = y_intercept(coord1, coord2)
    m2 = slope(coord3, coord4)
    b2 = y_intercept(coord3, coord4)

    # check if the lines are parallel
    if m1 == m2:
        return "no intersection"

    # compute the intersection point
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1

    # format the output as a fraction or an integer
    if is_fraction(x) or is_fraction(y):
        return f"({format_fraction(x)},{format_fraction(y)})"
    else:
        return f"({int(x)},{int(y)})"

def parse_coord(coord_str):
    # extract the x and y values from the coordinate string
    coord_str = coord_str.strip('()')
    x, y = map(int, coord_str.split(','))
    return (x, y)

def slope(coord1, coord2):
    # compute the slope of the line through the two coordinates
    x1, y1 = coord1
    x2, y2 = coord2
    return (y2 - y1) / (x2 - x1)

def y_intercept(coord1, coord2):
    # compute the y-intercept of the line through the two coordinates
    x, y = coord1
    m = slope(coord1, coord2)
    return y - m * x

def is_fraction(num):
    # check if a number is not an integer
    return num % 1 != 0

def format_fraction(num):
    # format a fraction as a string in the form "n/d"
    frac = Fraction(num).limit_denominator()
    n, d = frac.numerator, frac.denominator
    if n < 0:
        return f"-{-n}/{d}"
    else:
        return f"{n}/{d}"
