xfile = open('admission.txt')
count = 0

for line in xfile :
    count = count + 1
    line = line.rstrip()
    if line.startswith('Carol'):
        print(line)

    if 'mitha' in line:
        print(line)

print(count)