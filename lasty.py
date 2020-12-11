fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
lst = list()
dct = dict()
fst = list()
for line in fh:
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        else:
            line.rstrip()
            abc = line.split()
            for word in abc[5:6]:
                lst.append(word)
            for word in lst:
                bcd = word.split(':')
            for word in bcd[:1]:
                dct[word] = dct.get(word,0)+1
for k,v in dct.items():
    newtup = (k,v)
    fst.append(newtup)
fst = sorted(fst,reverse=False)
for k,v in fst:
    print(k,v)
