grades = {}

# key - value  데이터 삽입
grades["현승"] = 80
grades["태호"] = 60
grades["양훈"] = 90
grades["지웅"] = 70
grades["동욱"] = 96

# key를 이용해서 value 탐색
print(grades["동욱"])
print(grades["지웅"])

# key를 이용한 삭제
grades.pop("태호")
grades.pop("지웅")
