import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    """사용자가 단어를 입력 시 단어의 정의를 리턴하는 인터렉티브 영어 사전"""
    # 모든 문자를 소문자로 변경
    w = w.lower()
    # 혹 사용자가 오타 혹은 잘못된 스펠링을 입력한 경우, 유사한 단어를 찾는다.
    similar_word = get_close_matches(w, data.keys(), n = 1)[0]
    # 데이터 발견 시 정의 리턴
    if w in data:
        return data[w]
    # 앞에 대문자로 표기된 명사의 경우 
    elif w.title() in data:
        return data[w.title()]
    # 축약어로 전체가 다 대문자로 입력된 경우
    elif w.upper() in data:
        return data[w.upper()]
    # 유사한 단어가 사용자가 의도한 단어가 맞는지 확인한다.
    elif similar_word:
        YN = input(f"Did you meant {similar_word} instead? Enter Y if yes, or N if no.")
        if  YN == "Y" or YN == "y":
            return data[similar_word]
        elif YN == "N" or YN == "n":
            return "The word doesn't exsist. Please double check it."
        else:
            return "We didn't unerstand your entry."
    # 상기 경우에 모두 해당하지 않을 경우, 단어가 존재하지 않음을 회신한다.
    else:
        return "The word doesn't exsist. Please double check it."

word = input("Enter word: ")

output = translate(word)

# 리턴해야하는 값이 리스트인 경우, 보다 예쁘게 출력될 수 있도록 한다.
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
