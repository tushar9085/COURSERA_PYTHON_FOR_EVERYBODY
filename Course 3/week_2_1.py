import re

filehandle = open("Chuck.txt")

filestr = filehandle.read()

numstr = re.findall('[0-9]+',filestr)

sum = 0

for num in numstr:
    sum = sum + int(num)

print(sum)