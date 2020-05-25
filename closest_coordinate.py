from math import sqrt

def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

def closest_pair(coordinates):

    shortest_distance = distance(coordinates[1], coordinates[2])

    for i in range(len(coordinates)-1):
        for j in range(i+1, len(coordinates)):
            if  distance(coordinates[i], coordinates[j]) < shortest_distance:
                shortest_distance = distance(coordinates[i], coordinates[j])
                list = [coordinates[i], coordinates[j]]

    return list