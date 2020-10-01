import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(w):
    w = w.lower()

    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes, N for no" % get_close_matches(w, data.keys())[0])

        if yn == "Y":
            return data[get_close_matches(w, data.keys())]

        elif yn == 'N':
            return "The word doesn't exist. Please check it"

        else:
            return 'Sorry, We didnt underdstand your query'
    
    else:
        return "The word doesn't exist. Please check it"


word = input("Enter a Word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)