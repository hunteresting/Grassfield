def course_selection(course_list):

    recommendation = []

    while len(course_list) != 0:
        end_time = 20
        for lecture in course_list:
            if end_time > lecture[1]:
                temp = course_list.index(lecture)
                end_time = lecture[1]

        recommendation.append(course_list[temp])
        del course_list[temp]

        for overlap in course_list:
            if overlap[0] < recommendation[len(recommendation)-1][1]:
                del course_list[course_list.index(overlap)]

    return recommendation


print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
