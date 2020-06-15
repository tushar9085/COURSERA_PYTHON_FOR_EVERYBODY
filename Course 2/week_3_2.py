filename = input("Enter a file:") #mbox-short.txt

filehandle = open(filename)

tot = 0
count = 0

for lines in filehandle:
    if "X-DSPAM-Confidence:" in lines:
        foundline = lines
        pos = foundline.find(':')
        floatnumstr = foundline[pos+1:]
        floatnumstr.lstrip()
        count = count + 1
        tot = tot + float(floatnumstr)

avg = tot/count

print("Average spam confidence:",round(avg,12))