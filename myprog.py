smallest = None
largest = None
while True:
    x = input ('Enter a number:')
    if x == 'done':
        break
    try:
        y = float(x)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = y
    elif smallest > y:
        smallest = y
    if largest is None:
            largest = y
    elif largest < y:
            largest = y
large = int(largest)
small = int(smallest)
print('Maximum is',large)
print('Minimum is',small)
