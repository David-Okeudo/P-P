#this program analyses the first 100 numbers and sorts them into
# multiples of both 3 and 5, multiples of 3 and multiples of 5
for number in range(100+1):
    print(number)
    if number%3 == 0 and number%5 == 0:
        print("Nice shot")
    elif number%3 == 0:
        print("Nice")
    elif number%5 == 0:
        print("Shot")
    else:
        print("Trash")
quit()
