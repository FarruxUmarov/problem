# Function tuzing. Bu function, listning ichidagi 
# tuple ni listga o'girib bersin.

# Input:     [(1, 2), (2, 3), (3, 4)]
# Output:  [[1, 2], [2, 3], [3, 4]]

# —————————————————————————

# Input:     [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Output:  [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

num =  [(1, 2), (2, 3), (3, 4)]


for x in range(len(num)):
    num[x] = list(num[x])
print(num)