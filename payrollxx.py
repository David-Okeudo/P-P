hours = input('how many hours did you work?\n')
try :
  ihours = float(hours)
except :
    print ('Enter numeric input')

rate = input('rate per hour?\n')
try :
    irate = float(rate)
    if ihours == 40 :
        print (ihours*irate)
    elif ihours > 40 :
        orate = (ihours-40)*(1.5*irate)
        print ((40*irate) + orate)
except :
            print ('Enter numeric input')
