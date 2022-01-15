fname = input("Enter file name: ")
fhandle = open(fname,"r")
counter = 0
for line in fhandle:
    if line.startswith("From:"):
        counter = counter + 1
        splt = line.split()
        x = splt[1]
        print(x)
if len(fname) < 1:
    fname = "mbox-short.txt"

print("There were", counter, "lines in the file with From as
