from random import randint

# 파일 열기
in_file = open('vocabulary.txt', 'r')

# 사전 만들기
vocab = {}

for line in in_file:
    # 정보 정리
    data = line.strip().split(": ")
    english_word = data[0]
    korean_word = data[1]
    
    # 사전에 추가
    vocab[english_word] = korean_word
    
while True:
    keys = list(vocab.keys())
    index = randint(0, len(keys)-1)
    english_word = keys[index]
    korean_word = vocab[english_word]
    
    # 유저 입력값 받기
    guess = input(f"{korean_word}: ")
    
    # 끝내기
    if guess = "q":
        break
    
    # 정답 확인
    if guess == english_word:
        print("정답입니다\n")
    else:
        print(f"아쉽습니다. 정답은 {english_word}입니다.\n")
    
# 파일 닫기
in_file.close()