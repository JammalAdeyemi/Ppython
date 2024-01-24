from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        self.cost = self.cost.replace('$', '')
        self.cost = float(self.cost)
        self.quantity = int(self.quantity)
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"
       

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data(Shoe):
    while True:
        try:
            with open('inventory.txt', 'r') as file:
                file.readline()
                for line in file:
                    line = line.strip()
                    line = line.split(',')
                    shoe = Shoe(line[0], line[1], line[2], line[3], line[4])
                    shoe_list.append(shoe)
            break

        except FileNotFoundError:
            print('File not found. Please try again.')
            break

        except IndexError:
            print('Index error. Please try again.')
            break

def capture_shoes(Shoe):
    try:
        country = input("Enter the country of origin: ")
        code = input("Enter the code: ")
        product = input("Enter the product name: ")
        cost = float(input("Enter the cost: "))
        quantity = int(input("Enter the quantity: "))
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)

    except ValueError:
        print('Value error. Please try again.')
        
def view_all():
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    table = []
    for shoe in shoe_list:
        table.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])

    print(tabulate(table, headers, tablefmt="pretty"))

def re_stock():
    with open('inventory.txt', 'r+') as file:
        lines = file.readline()

    # find the shoe with the lowest quantity
    min_quantity = float('inf')
    min_line = None
    for line in lines:
        # Split the line into a list of values
        values = line.strip().split(',')
        # Check if the quantity is lower than the current minimum
        if int(values[4]) < min_quantity:
            min_quantity = int(values[4])
            min_line = line

    # Prompt the user for confirmation
    print(f"The shoe with the lowest quantity is {min_line.strip()}.")
    add_quantity = input("Do you want to add more stock? (yes/no): ").lower()

    # If the user wants to add more stock, update the file
    if add_quantity == 'yes':
        # Split the line into a list of values
        values = min_line.strip().split(',')
        # Prompt the user for the new quantity
        new_quantity = int(input("Enter the quantity to add: "))
        # Update the quantity
        values[4] = str(int(values[4]) + new_quantity)
        # Reconstruct the line with the new quantity
        new_line = ','.join(values) + '\n'
        # Find the index of the line to update
        index = lines.index(min_line)
        # Replace the old line with the new line
        lines[index] = new_line
        
        with open('inventory.txt', 'w') as file:
            file.writelines(lines)
        print("The stock has been updated.")
    else:
        print("The stock has not been updated.")

def search_shoe():
    code = input("Enter the code of the shoe: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
        else:
            print(f"No shoe found with the code {code}.")

def value_per_item():
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"The total value for shoe {shoe.code} is ${value:.2f}")

def highest_qty():
    max_quantity = 0
    max_shoe = None
    for shoe in shoe_list:
        if shoe.quantity > max_quantity:
            max_quantity = shoe.quantity
            max_shoe = shoe
    if max_shoe != None:
        print(f"The shoe with the highest quantity is {max_shoe.product}. It has {max_shoe.quantity} units in stock.")
    else:
        print("No shoes in the inventory.")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
def main_menu():
    while True:
        print("Shoe Inventory System")
        print("1. Read shoes data from file")
        print("2. Capture new shoe")
        print("3. View all shoes")
        print("4. Search for a shoe")
        print("5. Re-stock shoe with the lowest quantity")
        print("6. View shoe with highest quantity")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            read_shoes_data(Shoe)
        elif choice == "2":
            capture_shoes(Shoe)
        elif choice == "3":
            view_all(shoe_list)
        elif choice == "4":
            shoe = search_shoe()
            if shoe:
                print(shoe)
        elif choice == "5":
            re_stock()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Thank you for using the Shoe Inventory System.")
            break
        else:
            print("Invalid choice. Please try again.")
