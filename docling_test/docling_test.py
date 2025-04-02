from docling.document_converter import DocumentConverter
import csv
import re

# data 

source = "image.png"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)

# be sure to have input images correct

def remove_extra_spaces(text):
    return ' '.join([word for word in text.split() if word])

def is_invalid_charstring(text):
    x = re.search("^[a-zA-Z1-9]", text)
    return(x is None)

data = result.document.export_to_markdown()

lines = data.split("\n")

complete_lines=[]
headers = ['Headline', 'Publisher', 'Time']


for line in lines:
    line = remove_extra_spaces(line).strip()
    components = line.split("|")[1:4]
    shortest_component = min(components, key=len)
    if(len(components) != 3): continue
    if(len(shortest_component)==0): continue

    # issue 
    if(any(is_invalid_charstring(x) for x in components)):continue

    complete_lines.append(dict(zip(headers,components)))

    # we must remove the numbers
    
f = open('data.csv','w')
writer = csv.DictWriter(f, fieldnames=headers)
writer.writeheader()
writer.writerows(complete_lines)


