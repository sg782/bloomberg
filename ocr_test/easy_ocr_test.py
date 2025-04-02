import easyocr

# Create an OCR reader object
reader = easyocr.Reader(['en'])

# Read text from an image
result = reader.readtext('image.png')

lines = []

# Print the extracted text
for detection in result:
    lines.append(detection[1])

# print(lines)

f = open('data.txt','w')

for line in lines:
    print(line)
    f.write(line + "\n")