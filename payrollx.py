# WE WANT TO CREATE A MORE DETAILED payroll
hours = input('how many hours did you work?')
ihours = float(hours)
rate = input('rate per hour?')
irate = float(rate)
if ihours == 40 :
    print (ihours*irate)
elif ihours >= 40 :
    nrate = 1.055*rate
    print (ihours*nrate)
print ('congratulations')
