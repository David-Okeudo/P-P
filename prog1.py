fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
dct = dict()
k = None
v = None
for line in fh:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    line.rstrip()
    abc = line.split()
    for line in abc:
        if not '@' in line:
            continue
        else:
            dct[line] = dct.get(line,0) + 1
bigword = None
bigcount = None
for k,v in dct.items():
    if bigcount is None or v > bigcount:
        bigcount = v
        bigword = k
print(bigword,bigcount)
quit()
