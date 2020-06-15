
inp = input("Enter a file:")
filehandle = open(inp)

List = list()

for line in filehandle:
    line.rstrip()
    words = line.split()
    for word in words:
        if not word in List:
            List.append(word)


List.sort()
print(List)