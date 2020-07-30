import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    similar_word = get_close_matches(w, data.keys(), n = 1)[0]
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif similar_word:
        YN = input(f"Did you meant {similar_word} instead? Enter Y if yes, or N if no.")
        if  YN == "Y" or YN == "y":
            return data[similar_word]
        elif YN == "N" or YN == "n":
            return "The word doesn't exsist. Please double check it."
        else:
            return "We didn't unerstand your entry."
    else:
        return "The word doesn't exsist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
