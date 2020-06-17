import urllib.request, urllib.parse, urllib.error
import json

serviceUrl = "http://py4e-data.dr-chuck.net/json?"

address = input("Enter :")

parms = dict()
parms['key'] = 42
parms['address'] = address

url = serviceUrl + urllib.parse.urlencode(parms)

urlstr = urllib.request.urlopen(url).read().decode()

jsonInfo = json.loads(urlstr)

print(jsonInfo["results"][0]["place_id"])