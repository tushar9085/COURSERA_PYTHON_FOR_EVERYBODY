import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

htmlstr = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_628891.html').read()

soap = BeautifulSoup(htmlstr, "html.parser")

tags = soap('span')
sum = 0

for tag in tags:
    word = tag.contents[0]
    sum = sum + int(word)

print(sum)
