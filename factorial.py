import math
sen = int(input('please enter a number:'))
def factorial(sen):
    y = [i for i in reversed(range(sen+1))][:-1]
    print(math.prod(y))
factorial(sen)
