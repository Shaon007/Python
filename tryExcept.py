try:
    value = 10/0
    number = int(input("enter a number: "))
    print(number)
except ValueError:
    print("invalid Input")
except ZeroDivisionError as err:
    #print("Divided by zero")
    print(err)
