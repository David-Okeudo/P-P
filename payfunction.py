hours = input('how many hours did you work?\n')
x = float(hours)
rate = input('rate per hour?\n')
y = float(rate)
def computepay (ihours,irate) :
    #hours = input('how many hours did you work?\n')
    #ihours = float(hours)
    #rate = input('rate per hour?\n')
    #irate = float(rate)
    #money1 = (ihours*irate)
    #orate = (ihours-40)*(1.5*irate)
    #money2 = ((40*irate) + orate)
    if x==40 :
        money1 = (ihours*irate)
        return money1
    elif x>40 :
        orate = (ihours-40)*(1.5*irate)
        money2 = ((40*irate) + orate)
        return money2
money = computepay(45,10.5)
print ('Pay', money)
