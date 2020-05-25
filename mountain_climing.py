def select_stops(water_stops, capacity):
    
    answer = []
    water = capacity
    water_stops.insert(0, 0)


    for stop in range(1, len(water_stops)):
        water = water - water_stops[stop] + water_stops[stop - 1]
        if stop == len(water_stops) - 1:
            answer.append(water_stops[stop])
            return answer
        if water < water_stops[stop+1] - water_stops[stop]:
            answer.append(water_stops[stop])
            water = capacity
            
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))