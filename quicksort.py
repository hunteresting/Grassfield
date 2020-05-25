def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list

def partition(my_list, start, end):
    b = start
    for i in range(start, end):
        if my_list[i] < my_list[end]:
            swap_elements(my_list, i, b)
            b += 1
    swap_elements(my_list, b, end)
    return b

def quicksort(my_list, start, end):
    if end - start < 1:
        return
    else:
        p = partition(my_list, start, end)
        quicksort(my_list, start, p - 1)
        quicksort(my_list, p + 1, end)


list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)