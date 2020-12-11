# we want to create a result scheme
y = input('Enter score: ')
try :
    x = float(y)
    if x >= 0.0 and x <= 1.0 :
        if x >= 0.9 :
            print ('A')
        elif x >= 0.8 :
            print ('B')
        elif x >= 0.7 :
            print ('C')
        elif x >= 0.6 :
            print ('D')
        elif x <= 0.6 :
            print ('F')
    else :
            print ('Score is out of range')
except:
    print ('Score is not valid')
