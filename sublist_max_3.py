def sublist_max(profits):
    max_profit_so_far = profits[0] 
    max_check = profits[0] 
    print(max_profit_so_far)
    print(max_check)

    for i in range(1, len(profits)):
        print(f"max_check + profits[i] = {max_check + profits[i]}, profits[i] = {profits[i]}")
        max_check = max(max_check + profits[i], profits[i])
        print(f"max_check = {max_check}")

        max_profit_so_far = max(max_profit_so_far, max_check)
        print(f"max_check = {max_check}")
        print(f"max_profit_so_far = {max_profit_so_far}")
    
    return max_profit_so_far
    
    
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))