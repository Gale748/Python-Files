while True:
    try:
        num = int(input("Enter a number: "))
        print("The number you entered is:", num)
        if num == 0:
            print("The number is zero")
        elif num > 0:
            print("The number is positive")
        else:
            print("The number is negative")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")