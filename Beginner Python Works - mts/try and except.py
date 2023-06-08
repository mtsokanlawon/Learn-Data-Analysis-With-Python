try:
    number = int(input("Enter an integer: "))
    print(number)
except ValueError as err:
    print(err)