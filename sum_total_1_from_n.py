def triangle_number(n):
    if n == 0:
        return 0
    return triangle_number(n-1)+n

for i in range(1, 11):
    print(triangle_number(i))