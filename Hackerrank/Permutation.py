# The task is to write a python function called "PrintCycles(Perm)" that when given a permutation in the format below will output 
# a string representation of each cycle.
# Input format: A list of integers representing the permutation. [ f(1), f(2), f(3) ]. 
# For example, the permutation described above would be represented (as a python list) as: [ 5, 4, 3, 6, 7, 8, 1, 2 ]

# Output format: A list of strings representing cycles ordered such that:
# 1) Within each cycle the smallest number comes first
# 2) Cycles are ordered longest to shortest, and if multiple cycles have the same length they are ordered by the 
# smallest number within each cycle (smallest to largest)

# The output of the example above would therefore be: [ "(2 4 6 8)", "(1 5 7)", "(3)" ]

# Complete the 'PrintCycles' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER_ARRAY Perm as parameter.

def PrintCycles(Perm):
    # Write your code here
    n = len(Perm)
    visited = [False] * n
    cycles = []
    for i in range(n):
        if not visited[i]:
            cycle = []
            j = i
            while not visited[j]:
                visited[j] = True
                cycle.append(j+1)
                j = Perm[j] - 1 if 0 <= j < n else 0
            cycles.append(cycle)
    cycles = sorted(cycles, key=lambda x: (-len(x), min(x)))
    for i in range(len(cycles)):
        cycles[i] = "(" + ' '.join(map(str, cycles[i])) + ")"
    return cycles

# Explanation:

# 1. The function first initializes an empty list called cycles that will be used to store all the cycles in the permutation.
# 2. Then it iterates through the permutation and for each unvisited element, it starts a new cycle and follow the permutation 
# until it reaches the starting element again, adding all the visited elements to the current cycle.
# 3. After all the cycles are found, it sort the cycles based on the length of the cycle in descending order 
# and if the length is the same then sort the cycles based on the minimum element of the cycle, in ascending order.
# 4. Then it creates the required string representation of each cycle and append it to the output list.
# 5. Finally, it returns the output list.