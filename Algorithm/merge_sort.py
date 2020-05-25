def merge(list1, list2):

    i = 0
    j = 0

    merged_list = []

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    if i == len(list1):
        merged_list += list2[j:]

    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list


def merge_sort(my_list):
    
    if len(my_list) < 2:
        return my_list


    return merge(merge_sort(my_list[len(my_list)//2:]), merge_sort(my_list[:len(my_list)//2]))
    
    
    



print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))