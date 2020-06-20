import xml.etree.ElementTree as ET

stuff = ET.parse('Library.xml')
all = stuff.findall('dict/dict/dict')

found = False

for line in all:
    for child in line:

        if found==True:
            print(child.text)
            found = False
        if child.tag =='key' and child.text == 'Play Count':
            found = True