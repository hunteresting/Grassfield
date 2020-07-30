def sum_digit(num):
    num = str(num)
    sum = 0
    for i in range(len(num)):
       sum += int(num[i])
    return sum

count = 1
total = 0

while count < 1001:
    total += sum_digit(count)
    count += 1

print(total)