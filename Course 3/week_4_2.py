import urllib.request, urllib.parse ,urllib.error
from bs4 import BeautifulSoup

url = input("Enter URL:")
counts = input("Enter counts")
position = input("Enter positiopn:")

htmlstr = urllib.request.urlopen(url).read()

soap = BeautifulSoup(htmlstr, "html.parser")

tags = soap('a')

namelist = list()

for count in range(int(counts)):
    namelist.append(tags[int(position)-1].contents[0])
    htmlstr = urllib.request.urlopen(tags[int(position)-1].get('href', None)).read()
    soap = BeautifulSoup(htmlstr, "html.parser")
    tags = soap('a')

print(namelist[int(counts)-1])