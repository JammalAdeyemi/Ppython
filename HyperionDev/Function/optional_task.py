# Write a program that will act as a calculator.

# Create functions named add_num, subtract_num, multiply_num, and divide_num that asks the user to enter two numbers and adds, subtracts, multiplies, or divides them, respectively.
def add_num():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1 + num2

def subtract_num():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1 - num2

def multiply_num():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1 * num2

def divide_num():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1 / num2

# Print out the following menu and ask the user to input a number that corresponds to the option they would like to choose:
# ● Option 1 - add
# ● Option 2 - subtract
# ● Option 3 - multiply
# ● Option 4 - divide

# Main program
print("Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))

# If the user enters 1 call the add_num function
if choice == 1:
    result = add_num()
# If the user enters 2 call the subtract_num function
elif choice == 2:
    result = subtract_num()
# If the user enters 3 call the multiply_num function
elif choice == 3:
    result = multiply_num()
# If the user enters 4 call the divide_num function
elif choice == 4:
    result = divide_num()
# Make sure that the result of the calculation is printed out to the screen.
else:
    print("Invalid choice.")

if choice in [1, 2, 3, 4]:
    print(f"Result: {result}")
