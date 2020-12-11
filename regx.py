#Welcome David Okeudo from Using Python to Access Web Data

#Finding Numbers in a Haystack
#In this assignment you will read through
#and parse a file with text and numbers.
#You will extract all the numbers in the file
#and compute the sum of the numbers.

fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "regex_sum_756628.txt"
fh = open(fname)
y = list()
y.append('0')
v = int(0)
import re
for line in fh:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    y = y + x
for word in y:
    word = int(word)
    v = v + word
print(v)
