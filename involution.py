def power(x, y):
    if y == 1:
        return x  
    if y%2 == 0:
        print(f"power(x*x, y/2) = power({x*x}, {y/2}")
        return power(x*x, y/2)
    else:
        return x * power(x*x, (y-1)/2)
        
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))