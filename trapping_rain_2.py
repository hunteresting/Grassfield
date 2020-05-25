def check (buildings, line):
    full = 0
    start = 0
    finish = len(buildings) - 1

    for block in buildings:
        if block >= line:
            start = buildings.index(block)
            break
    
    buildings.reverse()
    for block in buildings:   
        if block >= line:
            finish = buildings.index(block)
            break

    for block in buildings:
        if block >= line:
            full += 1
    
    return len(buildings) - (finish + start) - full


def trapping_rain(buildings):
    
    max = 0
    for item in buildings:
        if item > max:
            max = item
            
    answer = 0
    while max != 0:
        answer += check(buildings, max)
        max -= 1
        
    return answer
                

print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))