# we want to do some string operations
text = "X-DSPAM-Confidence:      0.8475     "
atpos = text.find('0')
spos = text.find('5')
texty = text[atpos:spos+1]
print(float(texty))
