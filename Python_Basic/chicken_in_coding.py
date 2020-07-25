# 매출 파일 열기
chicken = open('data/chicken.txt', 'r')

# 총 매출
sum = 0
count = 0

# 파일의 각 줄 읽기
for i in chicken:
    temp = []
    temp = i.split("일: ")
    sum += int(temp[1])
    count += 1
    
print(sum/count)

#파일 닫기
chicken.close()