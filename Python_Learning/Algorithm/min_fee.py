def min_fee(pages_to_print):
    
    time = 0
    pages_to_print = sorted(pages_to_print)
    
    for page in range(len(pages_to_print)):
        time += pages_to_print[page] * (len(pages_to_print)-page)

        
    return time
    

print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))