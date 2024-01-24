# A newly created medical test, the purpose of which is to diagnose a rare disease, has been tested on a group of N patients. 
# For each patient, the test may be either positive or negative, but the result might not always be correct 
# (e.g. a person with a positive test result may in fact not be ill). Having information about the real state of health of each 
# patient and the result of the new test, we want to calculate its quality; that is, its sensitivity and specificity.

# Write a function: def solution(A,B,q)

# that, given two arrays of binary values A and B, both of length N, representing the real state of patients and the test results, where 0 corresponds to negative result and 1 to positive one, returns either sensitivity of the test (when q is False) or Specificity of the test (when q is True).
# Example test cases:
# A = [1,0,1,1,0,1], B = [0,1,1,0,0,1], Q = False: expected answer 0.5
# A= [1,0,0,1,0,1,1,0], B=[1,1,0,1,1,1,0,1], q= True: expected answer 0.25

def solution(A, B, q):
    # Initialize variables to count true positives, true negatives, false positives, and false negatives.
    true_positives = 0
    true_negatives = 0
    false_positives = 0
    false_negatives = 0

    # Iterate through the arrays A and B to compare the real state and test results.
    for real_state, test_result in zip(A, B):
        if real_state == 1 and test_result == 1:  # True Positive
            true_positives += 1
        elif real_state == 0 and test_result == 0:  # True Negative
            true_negatives += 1
        elif real_state == 0 and test_result == 1:  # False Positive
            false_positives += 1
        elif real_state == 1 and test_result == 0:  # False Negative
            false_negatives += 1

    if q:  # Calculate Specificity
        return true_negatives / (true_negatives + false_positives)
    else:  # Calculate Sensitivity
        return true_positives / (true_positives + false_negatives)


### SQL
# POSTGRESQL
# You are given two tables, flights and airports, with the following structure:

# flights
# start_port - char(3) NOT NULL
# end_port - char(3) NOT NULL

# airports
# city_name - varchar(17) NOT NULL
# port_code - varchar(17) NOT NULLchar(3) NOT NULL

# Each row in the table flights contains information about a flight: code of departure port (start_port) and code of destination port (end_port).

# Each row in the table airports contains information about an airport: the city name (city_name) and the port code (port_code). Each port_code is assigned to at most one airport.

# Write an SQL query that finds all cities through which a flight from New York to Tokyo may pass if the passenger wants to make exactly one change of flights.

# Example:
# For given tables FLIGHTS
# Start_port - end_port
# JFK - NRT
# LGA - LAX
# LAX - HND
# LAX - HND
# JFK - CDG
# CDG - MUC
# JFK - HND
# JFK - MUC
# MUC - NRT

# and AIRPORTS
# city_name - port_code
# New York - JFK
# New York - LGA
# Paris - CDG
# Tokyo - HND
# Los Angeles - LAX
# Tokyo - NRT
# Munich - MUC

# Your query should return:

# Cities:
# Los Angeles
# Munich

# Assume that: there are no flights with the same start_port and end_port

# Write the code in SQLLite

# SELECT DISTINCT a1.city_name
# FROM flights as f1
# JOIN airports as a1 on f1.end_port = a1.port_code
# WHERE f1.start_port IN (
#     SELECT port_code FROM airports WHERE city_name = 'New York'
# )
# AND EXISTS (
#     SELECT 1 FROM flights as f2
#     JOIN airports as a2 on f2.end_port = a2.port_code
#     WHERE f2.start_port = f1.end_port and a2.city_name = 'Tokyo'
# )
# AND a1.city_name != 'New York'
# AND a1.city_name != 'Tokyo';