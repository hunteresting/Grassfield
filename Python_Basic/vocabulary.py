# 파일 열기
out_file = open('vocabulary.txt', 'w')

while True:
    # 영어 단어 입력
    english_word = input("영어 단어를 입력하세요: ")
    
    # "q" 입력 시 끝
    if english_word == "q":
        break
    
    # 한국어 뜻 입력
    korean_word = input("한국어 뜻을 입력하세요: ")
    
    # "q" 입력 시 끝
    if korean_word == "q":
        break