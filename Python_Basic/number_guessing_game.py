from random import randint

# 상수
NUM_TRIES = 4
ANSWER = randint

# 변수
tries = 0
guess = -1

while tries < NUM_TRIES and guess != ANSWER:
    guess = int(input(f"기회가 {NUM_TRIES - tries}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: "))
    tries += 1
    
    if guess < ANSWER:
        print("Up")
    elif guess > ANSWER:
        print("Down")

if guess == ANSWER:
    print(f"축하합니다. {tries}번만에 숫자를 맞추셨습니다.")
else:
    print(f"아쉽습니다. 정답은 {ANSWER}였습니다.")