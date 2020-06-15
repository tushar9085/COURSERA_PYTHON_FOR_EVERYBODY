inp = input("Enter a file:")
filehandle = open(inp)

count = 0

for line in filehandle:
    line.rstrip()
    if line.startswith('From'):
        if not line.startswith('From:'):
            words = line.split()
            print(words[1])
            count = count + 1

print("There were",count,"lines in the file with From as the first word")

