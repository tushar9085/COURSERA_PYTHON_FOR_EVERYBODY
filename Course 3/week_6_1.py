import urllib.request, urllib.parse, urllib.error
import json

url = "http://py4e-data.dr-chuck.net/comments_628894.json"

urlstr = urllib.request.urlopen(url).read()

jsonInfo = json.loads(urlstr)
sum = 0

for item in jsonInfo["comments"]:
    num = int(item["count"])
    sum += num

print(sum)