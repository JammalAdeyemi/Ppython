import datetime
import sys

def login():
    login = input('Enter your username: ').lower()
    password = input('Enter your password: ').lower()
    user_type = None

    # Open the file in read mode
    with open('user.txt', 'r+') as file:
        users = file.readlines()
        for user in users:
            user_info = user.split(', ')
            if login == user_info[0] and password == user_info[1]:
                user_type = user_info[2].strip()
                break
        if user_type is None:
            print('Invalid username or password, please try again')
            sys.exit()
        else:
            return user_type
            

def menu():
    user_type = login()
    if user_type == 'user':
        while True:
            menu = input('''Select one of the following Options below:
            a - Adding a task
            va - View all tasks
            vm - view my task
            e - Exit
            : ''').lower()
            if menu == 'a':
                add_menu()
                return
            elif menu == 'va':
                view_all()
                return
            elif menu == 'vm':
                view_mine()
                return
            elif menu == 'e':
                sys.exit()
            else:
                print('Invalid option, please try again')
            pass
            
    else:
        while True:          
            menu = input('''Select one of the following Options below:
            r - Registering a user
            a - Adding a task
            va - View all tasks
            vm - view my task
            gr - Generate report
            ds - Display statistics
            e - Exit
            : ''').lower()
            if menu == 'r':
                reg_user()
                return
            elif menu == 'a':
                add_menu()
                return
            elif menu == 'va':
                view_all()
                return
            elif menu == 'vm':
                view_mine()
                return
            elif menu == 'gr':
                generate_report()
                return
            elif menu == 'ds':
                display_statistics()
                return
            elif menu == 'e':
                sys.exit()
            else:
                print('Invalid option, please try again')
            pass

def reg_user():
    new_user = input('Enter a new username: ').lower()
    new_password = input('Enter a new password: ').lower()
    confirm_password = input('Confirm your password: ').lower()
    user_type = input('Enter the user type (admin/user): ').lower()

    # Check if the new password and confirmed password are the same.
    if new_password != confirm_password:
        print('Password does not match, please try again')
        return

    # Open the file in read mode
    with open('user.txt', 'r') as file:
        # Read the contents of the file
        users = file.readlines()
        # Check if the new username already exists in the file
        for user in users:
            if new_user in user:
                print('Username already exists, please try a different one')
                return

    # If the new username is unique, write it to the file along with the password
    with open('user.txt', 'a') as file:
        file.write(f'\n{new_user}, {new_password}, {user_type}')
        print(f'Successfully registered user: {new_user}')

def add_menu():
    # Request the user to input the username of the person the task is assigned to
    assigned_user = input('Enter the username of the person the task is assigned to: ')

    # Request the user to input the title of the task
    task_title = input('Enter the title of the task: ')

    # Request the user to input the description of the task
    task_description = input('Enter the description of the task: ')

    # Request the user to input the due date of the task
    task_due_date = input('Enter the due date of the task (10 Oct 2019): ')

    # get the current date
    current_date = datetime.datetime.now().strftime("%d %b %Y")

    # Request the user to input the status of the task
    task_status = 'No'

    # Write the data to the task.txt file
    with open('tasks.txt', 'a') as file:
        file.write(f'\n{assigned_user}, {task_title}, {task_description}, {task_due_date}, {current_date}, {task_status}')
        print(f'Successfully added task: {task_title}')
    pass

def view_all():
    # Read a line from the file
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()
        if len(tasks) == 0:
            print('No tasks to display')
            return
        for task in tasks:
            print(task)

def view_mine():
    username = input("Enter your username: ")
    task_list = []
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    for task in tasks:
        task_info = task.split(", ")
        if task_info[0] == username:
            task_list.append(task_info)

    if len(task_list) == 0:
        print("You have no tasks assigned to you.")
    else:
        print("Tasks assigned to you:")
        for i, task in enumerate(task_list):
            print(f"{i+1}. {task[1]} - Due on {task[3]} - Completed: {'Yes' if task[5].strip() == 'Yes' else 'No'}")
        
        task_num = int(input("Enter the number of the task you want to manage or -1 to return to main menu: "))
        if task_num == -1:
            return
        elif task_num < 1 or task_num > len(task_list):
            print("Invalid task number. Please try again.")
            return
        else:
            task = task_list[task_num-1]
            if task[5].strip() == 'Yes':
                print("This task has already been completed.")
                return
            else:
                task_manage = input("Enter 'c' to mark task as complete or 'e' to edit task: ")
                if task_manage == 'c':
                    task[5] = 'Yes'
                    with open("tasks.txt", "w") as file:
                        for t in task_list:
                            file.write(", ".join(t))
                    print("Task has been marked as complete.")
                elif task_manage == 'e':
                    task_edit = input("Enter 'u' to edit username or 'd' to edit due date: ")
                    if task_edit == 'u':
                        task[0] = input("Enter the new username: ")
                    elif task_edit == 'd':
                        task[3] = input("Enter the new due date: ")
                    else:
                        print("Invalid option. Please try again.")
                        return
                    with open("tasks.txt", "w") as file:
                        for t in task_list:
                            file.write(", ".join(t))
                    print("Task has been edited.")
                else:
                    print("Invalid option. Please try again.")
                    return

def generate_report():
    tasks = []
    users = []
    # Read the task data from the file
    with open('tasks.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            task = line.strip().split(', ')
            tasks.append(task)
            users.append(task[0])
    # Get the total number of tasks and completed tasks
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task[5] == 'Yes'])
    uncompleted_tasks = total_tasks - completed_tasks
    # get the current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    overdue_tasks = len([task for task in tasks if task[5] == 'No' and task[3] < current_date])
    incomplete_percent = (uncompleted_tasks / total_tasks) * 100
    overdue_percent = (overdue_tasks / total_tasks) * 100
    # Write the task overview data to the file
    with open("task_overview.txt", "w") as file:
        file.write("Task Overview:\n")
        file.write("Total number of tasks: " + str(total_tasks) + "\n")
        file.write("Total number of completed tasks: " + str(completed_tasks) + "\n")
        file.write("Total number of uncompleted tasks: " + str(uncompleted_tasks) + "\n")
        file.write("Total number of overdue tasks: " + str(overdue_tasks) + "\n")
        file.write("Percentage of incomplete tasks: {:.2f}%\n".format(incomplete_percent))
        file.write("Percentage of overdue tasks: {:.2f}%\n".format(overdue_percent))

    # Create a dictionary to store the user data
    user_data = {}
    for user in set(users):
        user_data[user] = [0, 0, 0, 0]
    for task in tasks:
        user_data[task[0]][0] += 1
        if task[5] == 'Yes':
            user_data[task[0]][1] += 1
        elif task[3] < current_date:
            user_data[task[0]][3] += 1
        else:
            user_data[task[0]][2] += 1

    # Write the user overview data to the file        
    with open("user_overview.txt", "w") as file:
        file.write("User Overview:\n")
        file.write("Total number of users: " + str(len(set(users))) + "\n")
        file.write("Total number of tasks: " + str(total_tasks) + "\n")
        for user in user_data:
            file.write("\nUser: " + user + "\n")
            file.write("Total number of tasks assigned: " + str(user_data[user][0]) + "\n")
            file.write("Percentage of total tasks assigned: {:.2f}%\n".format((user_data[user][0] / total_tasks) * 100))
            file.write("Percentage of tasks completed: {:.2f}%\n".format((user_data[user][1] / user_data[user][0]) * 100))
            file.write("Percentage of tasks still to be completed: {:.2f}%\n".format((user_data[user][2] / user_data[user][0]) * 100))
            file.write("Percentage of overdue tasks: {:.2f}%\n".format((user_data[user][3] / user_data[user][0]) * 100))

    print('Report generated successfully')
    pass

def display_statistics():
    try:
        with open("task_overview.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("task_overview.txt not found. Generating reports...")
        generate_report()
        with open("task_overview.txt", "r") as file:
            print(file.read())
    try:
        with open("user_overview.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("user_overview.txt not found. Generating reports...")
        generate_report()
        with open("user_overview.txt", "r") as file:
            print(file.read())
    pass

def exit():
    print('Exiting the program...')
    pass

# login()
menu()