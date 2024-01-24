import time
time.time()

timestamp1 = time.time()

### Python Program to find Sum of N Natural Numbers ###
num = 100
total = 0

for value in range(1, num + 1):
    total = total + value
    
print("The sum is", total)
### Program End ###
timestamp2 = time.time()
print("Time taken by for loop is", timestamp2 - timestamp1)