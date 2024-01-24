## Big 0(n) Complexity ##
student_list1 = ['tim', 'drake', 'ashish', 'shubham']
student_list2 = ['andrew', 'chris', 'harshit', 'lary', 'shubham']

def check_student(student_list1):
    for student in student_list1:
        if student == 'shubham':
            print('Available')
            
check_student(student_list1)
## Big 0(n) Ends ##

## Big 0(1) Complexity ##
student_list = ['andrew', 'akshat', 'chris', 'harshit', 'lary', 'shubham', 'tim', 'drake', 'ashish']
def displayStudent(student_list):
    print(student_list[0]) # O(1)
    print(student_list[1]) # O(1)
    
displayStudent(student_list) # O(1) - constant time
## Big 0(1) Ends ##

## Counting Operations ##
students = ['andrew', 'akshat', 'chris', 'harshit', 'lary', 'shubham', 'tim', 'drake', 'ashish'] # O[1]
def randomFunction(students):
    first = students[0] # O[1]
    total = 0 # O[1]
    new_list = [] # O[1]
    
    for student in students:
        total += 1 # O[n]
        new_list.append(student) # O[n]
    
    print(new_list) # O[1]
    return total # O[1]

print(randomFunction(students)) # O[6 + 2n] => O[n]
## Counting Operations Ends ##

## Big O(n^2) Complexity ##
num_list = [1, 2, 3, 4, 5, 6, 7]

def randomNumber(num_list):
    total = 0
    for num1 in num_list:
        for num2 in num_list:
            print(num1, num2)
            total += 1
    return total
print(randomNumber(num_list))   
## Big O(n^2) Ends ##

## Rule 5: Drop Non Dominants ##
num_list = [1, 2, 3, 4, 5, 6, 7]
def randomFunction(num_list):
    total = 0 # O[1]
    all_integer = True #O[1]
    for num in num_list:
        print(num) #O[n]
        
    for num1 in num_list:
        for num2 in num_list:
            print(num1, num2) #O[n^2]
            total += 1 #O[n^2]
    msg = "Rule 5 - Remove all non-dominant terms" #O[1]
    return total, msg #O[1]
        
print(randomFunction(num_list)) #O[4 + n + 2n^2] = O(n + 2n^2) = O(2n^2) => O(n^2)
## Rule 5 Ends ##