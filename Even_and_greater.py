"Interactive Even Number Validator with Custom Feedback"

a = int(input("Enter your two digit number: "))

if a % 2 == 0:
    print("It's an even number.")
    if a > 30:
        print("Number is greater than 30..")
        print("I love your choice of number.")

else:
    print("Pls, make another attempt.")