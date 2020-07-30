def sum_digits(n):
    i = str(n)
    if len(i) == 1:
        return n
    return sum_digits(int(n/10)) + int(i[len(i)-1])
    
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))