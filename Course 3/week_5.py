
      #PARSING XML DATA

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

htmlstr = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_628893.xml').read()

tree = ET.fromstring(htmlstr)

commentsList = tree.findall("comments/comment")

sum = 0

for comment in commentsList:
    value = comment.find("count").text
    sum += int(value)

print(sum)
