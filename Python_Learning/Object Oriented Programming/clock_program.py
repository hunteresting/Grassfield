class Counter:

    def __init__(self, limit):
 
        self.limit = limit
        self.value = 0


    def set(self, new_value):

        if 0 <= new_value < self.limit:
            self.value = new_value
        else:
            self.value = 0


    def tick(self):
        
        self.value += 1

        if self.value == self.limit:
            self.value = 0
            return True
        return False


    def __str__(self):
        
        return str(self.value).zfill(2)
    

class Clock:
    """
    시계 클래스
    """
    HOURS = 24 # 시 최댓값
    MINUTES = 60 # 분 최댓값
    SECONDS = 60 # 초 최댓값

    def __init__(self, hour, minute, second):
        
        self.hour = hour
        self.minute = minute
        self.second = second

    def set(self, hour, minute, second):
        
        self.hour = hour
        self.minute = minute
        self.second = second

    def tick(self):

        if self.second < 59 and self.minute <= 59:
            self.second += 1
        elif self.second < 59 and self.minute < 59:
            self.second += 1
        elif self.second >= 59 and self.minute < 59:
            self.second = 0
            self.minute += 1
        elif self.hour >= 23:
            self.second = 0
            self.minute = 0
            self.hour = 0
        else:
            self.second = 0
            self.minute = 0
            self.hour += 1


    def __str__(self):
        
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}"

# 초가 60이 넘을 때 분이 늘어나는지 확인하기
print("시간을 1시 30분 48초로 설정합니다")
clock = Clock(1, 30, 48)
print(clock)

# 13초를 늘린다
print("13초가 흘렀습니다")
for i in range(13):
    clock.tick()
print(clock)

# 분이 60이 넘을 때 시간이 늘어나는지 확인
print("시간을 2시 59분 58초로 설정합니다")
clock.set(2, 59, 58)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)

# 시간이 24가 넘을 때 00:00:00으로 넘어가는 지 확인
print("시간을 23시 59분 57초로 설정합니다")
clock.set(23, 59, 57)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)