
#spliting words from a file

filehandle = open('tushar.txt')

filestring = filehandle.read()

print(filestring)

filewords = filestring.split()

print(filewords)

for word in filewords:
    print(word)

#yeah that is cool

#Creating List

ListCreate = list()

for i in range(5):
    inp = input("Enter a numer :")
    ListCreate.append(float(inp))

ListCreate.sort()

print(ListCreate)

print(type(ListCreate[0]))

ListCreate.remove(5)

print(ListCreate)

#creationg dictionary

counts = dict()

for name1 in filewords:
    if name1 in counts:
        counts[name1] = counts[name1] + 1
    else:
        counts[name1] = 1

print(counts)

#shortcut of above is under ..by get method

for name in filewords:
    counts[name] = counts.get(name,0)+1

print(counts)

bigkey = None
bigvalue = None

for keys,values in counts.items():
    if bigvalue is None or bigvalue<values:
        bigkey = keys
        bigvalue = values

print(bigkey,bigvalue)

