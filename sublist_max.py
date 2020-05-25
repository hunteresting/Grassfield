def sublist_max(profits):

    profit_date = []
    for order in range(len(profits)):
        if profits[order] > 0:
            profit_date.append(order)

    sum2 = 0
    for a in profit_date:
        for b in profit_date:
            sum1 = 0
            print(f"a = {a}. b = {b}")
            if a == b or a > b:
                pass
            else:
                for c in range(a, b+1):
                    sum1 += profits[c]
                if sum1 > sum2:
                    sum2 = sum1
    
    return sum2




# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))