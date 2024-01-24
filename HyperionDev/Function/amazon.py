def min_of_list(lst):
    return min(lst)

def max_of_list(lst):
    return max(lst)

def avg_of_list(lst):
    return sum(lst) / len(lst)

def main():
    with open("input.txt", "r", encoding='utf-8') as in_file:
        with open("output.txt", "w") as out_file:
            for line in in_file:
                operation, numbers = line.strip().split(":")
                numbers = [int(x) for x in numbers.split(",")]
                if operation == "min":
                    result = min_of_list(numbers)
                elif operation == "max":
                    result = max_of_list(numbers)
                elif operation == "avg":
                    result = avg_of_list(numbers)
                else:
                    result = "Invalid operation"
                out_file.write(f"The {operation} of {numbers} is {result}\n")

if __name__ == "__main__":
    main()
