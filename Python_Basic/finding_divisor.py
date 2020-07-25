i = 1
count = 0

while i <= 120:
    if 120 % i == 0:
        print(i)
        count += 1
    else:
        pass
    i += 1

print(f"120의 약수는 총 {count}개입니다.")