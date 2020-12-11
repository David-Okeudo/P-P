fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    abc = line.split()
    for obj in abc:
        if obj in lst:
            continue
        lst.append(obj)
lst.sort()
print(lst)
