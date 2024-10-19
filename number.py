try:
    number = int(input("Enter your number(1-10) only: "))
    
    if (number == 1):
        print("One")
    elif (number == 2):
        print("Two")
    elif (number == 3):
        print("Three")
    elif (number == 4):
        print("Four")
    elif (number==5):
        print("Five")
    elif (number==6):
        print("Six")
    elif (number==7):
        print("Seven")
    elif (number==8):
        print("Eight")
    elif (number==9):
        print("Nine")
    elif (number==10):
        print("Ten")
    else:
        print("Wrong input!")
except ValueError:
    print("Invalid input! Please enter a valid number.")
