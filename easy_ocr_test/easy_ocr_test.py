import easyocr

reader = easyocr.Reader(['en'])


result = reader.readtext('./headlines.png')

for detection in result:
    print(detection[1])