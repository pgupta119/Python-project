import json
from difflib import get_close_matches

data=json.load(open("data.json","r"))
def load_data(dic):
    dic=dic.lower()
    if dic in data:
     return data[dic]
    elif dic.title() in data:
        return data[dic.title()]
    elif dic.upper() in data: 
        return data[dic.upper()]
    elif len(get_close_matches(dic,data.keys())) > 0:
        yn= input("Did you mean %s instead? Y for if yes  or N if No " % get_close_matches(dic,data.keys())[0])
        if yn =="Y":
            return data[get_close_matches(dic,data.keys())[0]]
        else:
            return  "No didnt understand you word"     
    else :
         return "The word does not exist. Please double check it"


word=[]
while True :
    if word =="\end":
        break
    else:
        word=input("Enter the word for meaning: ")
        output= load_data(word)
        if type(output)==list:
            for item in output:
                print(item)
        else:
            print(output)