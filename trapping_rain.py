def trapping_rain(buildings):

    drops = 0

    for i in range(1, len(buildings)-1):

        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        water = min(max_left, max_right)

        drops += max(0, water - buildings[i])

    return drops



print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))