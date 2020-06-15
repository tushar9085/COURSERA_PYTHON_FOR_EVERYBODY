inp = input("Enter a file:")

filehandle = open(inp)

nameList = list()

for line in filehandle:
    line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        nameList.append(words[1])

nameCounter = dict()

for name in nameList:
    nameCounter[name] = nameCounter.get(name,0)+1

bigName = None
bigValue = None

for name,value in nameCounter.items():
    if bigValue is None or bigValue<value:
        bigName = name
        bigValue = value

print(bigName,bigValue)