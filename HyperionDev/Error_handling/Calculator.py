# Create a simple calculator application that asks a num to enter two numbers and the operation (e.g. +, -, x, etc.) that they’d like to perform on the numbers. 
# Display the answer to the equation. Every equation entered by the num should be written to a text file. 
# Use defensive programming to write this program in a manner that is robust and handles unexpected events and num inputs.
def calculator():
    while True:
        try:
            num = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            operation = input('''Select one of the following Operations:
                + - Addition
                - - Subtraction
                x - Multiplication
                / - Division
                % - Percentage
                ** - Exponent
                // - Floor Division
                Enter your choice: ''')
                
            if operation == "+":
                result = num + num2
            elif operation == "-":
                result = num - num2
            elif operation == "x":
                result = num * num2
            elif operation == "/":
                result = num / num2
            elif operation == "%":
                result = num % num2
            elif operation == "**":
                result = num ** num2
            elif operation == "//":
                result = num // num2
            else:
                print("Invalid operator. Please enter a valid operator.")
                continue

            equation = str(num) + " " + operation + " " + str(num2) + " = " + str(result)
            print(f"{num} {operation} {num2} = {result}")

            with open("equations.txt", "a") as file:
                file.write(equation + "\n")
                print("Equation saved to file.")

# Now extend your program to give the num the option to either enter two numbers and an operator, like before or to read all of the equations from a
# new txt file (the num should add the name of the txt file as an input) and print out all of the equations together with the results. 
# Use defensive coding to ensure that the program does not crash if the file does not exist and that the num is prompted again to enter the name of the file.           
            choice = input("Enter 1 to enter two numbers and an operator or 2 to read equations from a file: ")
            if choice == "1":
                continue
            elif choice == "2":
                file_name = input("Enter the name of the file: ")
                try:
                    with open(file_name, "r") as file:
                        equations = file.readlines()
                        for equation in equations:
                            print(equation)
                except FileNotFoundError:
                    print("File not found. Please enter a valid file name.")
                    continue
        
        except ZeroDivisionError:
            print("Invalid input. Please enter a valid operator.")
            continue
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue



calculator()

