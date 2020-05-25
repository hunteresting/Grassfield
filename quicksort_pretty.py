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

def quicksort(my_list, start = 0, end = len(my_list) - 1):
        
    if end - start < 1:
        return my_list
        
    else:
        p = partition(my_list, start, end)
        quicksort(my_list, start, p - 1)
        quicksort(my_list, p + 1, end)
        

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)