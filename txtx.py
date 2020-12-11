# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
x = 0
for line in fh:
    if not "X-DSPAM-Confidence:" in line :
        continue
    atpos = line.find('0')
    texty = line[atpos:atpos+7]
    for line in texty:
        count = count + 1
        texty2 = float(texty)
        x = x + texty2
print(x)
print(count)
avg = x/count
print('Average spam confidence:',avg)
quit()
    #avg = (float(x))/count
#print("Average spam confidence:", avg)
