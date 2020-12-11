fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
count = 0
fh = open(fname)
lst = list()
for line in fh:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    count = count + 1
    line.rstrip()
    abc = line.split()
    print(abc[1])
print("There were", count, "lines in the file with From as the first word")
