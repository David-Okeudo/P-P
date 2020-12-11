def computepay (ihours,irate) :
    if x==40 :
        money1 = (ihours*irate)
        return money1
    elif x>40 :
        orate = (ihours-40)*(1.5*irate)
        money2 = ((40*irate) + orate)
        return money2
hrs = input('how many hours did you work?')
x = float(hrs)
rate = input('rate per hour?')
y = float(rate)
money = computepay(x,y)
print ('Pay', money)
