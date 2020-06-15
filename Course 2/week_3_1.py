
fname = input("Enter the file name:")
handlefile = open(fname)

filestr = handlefile.read()

filestr.rstrip()

filestrUpper = filestr.upper()

print(filestrUpper)