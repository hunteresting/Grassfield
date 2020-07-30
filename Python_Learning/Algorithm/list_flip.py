def flip(some_list):
    temp = []
    if len(some_list) == 1:
        return some_list
    temp.append(some_list[-1])
    return temp + flip(some_list[:-1])
    
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)