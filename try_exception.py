
try:
    number = int(input("Enter a number: "))
    value = 10/number
    print(value)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")
