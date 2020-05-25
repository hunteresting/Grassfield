def find_same_number(some_list):

    for i in range(len(some_list)):
        if some_list[i] in some_list[i+1:]:
            return some_list[i]


print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))