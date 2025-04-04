import re

def is_invalid_charstring(text):
    x = re.search("[a-zA-Z1-9]", text)
    return(x is None)

resp = "test"

while resp is not -1:
    print(resp)
    print(is_invalid_charstring(resp))
    print("---=----=--")
    resp = input("would you like to do another: ")