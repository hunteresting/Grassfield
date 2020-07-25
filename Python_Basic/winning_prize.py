year = 1988
prize = 50000000
apartment = 1100000000

while year < 2016:
    prize = prize * 1.12
    year += 1

if prize > apartment:
    print(f"{int(prize - apartment)}원 차이로 동일 아저씨의 말씀이 맞습니다.")
elif prize < apartment:
    print(f"{int(apartment - prize)}원 차이로 미란 아주머니의 말씀이 맞습니다.")
else:
    pass
