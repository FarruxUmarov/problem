# List ichidagi har bir tuple qiymatlarinig 
# yig'indisini yangi listga joylashtiradigan 
# funksiya yozing.

# Input:     [(1, 2), (2, 3), (3, 4)]
# Output:  [3, 5, 7]

# —————————————————————————

# Input:      [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
# Output:   [9, -1, 7, 8]


tuple_lst =  [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

for tup in tuple_lst:
    num = sum(tup)
    print(num)