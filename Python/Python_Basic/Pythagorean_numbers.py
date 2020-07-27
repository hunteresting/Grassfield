for a in range(1, 332):
    for b in range(a, 498):
        c = 1000 - a - b
        if a * a + b * b == c * c and a + b + c == 1000 and a < b:
            print(a * b * c)
            break