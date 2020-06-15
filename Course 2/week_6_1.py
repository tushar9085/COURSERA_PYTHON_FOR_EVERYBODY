inp = input("Enter a file:")

filehandle = open(inp)

hourList = list()

for line in filehandle:
    line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        time = words[5]
        hourList.append(time[:2])


hourCount = dict()

for hour in hourList:
    hourCount[hour] = hourCount.get(hour,0)+1

#sorting with key values

sortedlist = sorted(hourCount.items())
print(sortedlist)

#sorting with values:

tmplist = list()
for k,v in hourCount.items():
    tmplist.append((v,k))

sortedlistValue = sorted(tmplist,reverse=True)
print(sortedlistValue)

