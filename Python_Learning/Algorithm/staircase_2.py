def staircase(stairs, possible_steps):
    if stairs == 0:
        return 1
        
    sum = 0
  
    for val in possible_steps:
        if val <= stairs:
            sum += staircase(stairs - val, possible_steps)
    return sum
    
print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))