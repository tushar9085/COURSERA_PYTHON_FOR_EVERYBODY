filehandle = open('mbox-short.txt')

filestring = filehandle.read()
fileList = filestring.split()

wordCounter = dict()
for word in fileList:
    wordCounter[word] = wordCounter.get(word,0)+1

wordCounterList = wordCounter.items()  #This gives us a tuple of list

reversedwordCounterList = list()

for k,v in wordCounterList:          #alter the key value to value key,as tuple sort the first item first
    reversedwordCounterList.append((v,k))

sortedList = sorted(reversedwordCounterList,reverse=True)   #the list is sorted by value order...now we can select the top 10 higeghest values

for v,k in sortedList[:20]:
    print(k,v)


