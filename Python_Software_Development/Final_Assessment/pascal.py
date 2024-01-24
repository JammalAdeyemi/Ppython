# Create a Python file called pascal.py to ask for the height of Pascal’s triangle (the height is the number of rows in the triangle), 
# then generate the triangle and output it in the same style as in Figure above.
user = int(input("Please enter the triangle's height: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

for i in range(user):
    print(" " * (user - i), end = "")
    
    for j in range(i + 1):
        print("{0:4d}".format(int(factorial(i) / (factorial(j) * factorial(i - j)))), end = "")
    print()