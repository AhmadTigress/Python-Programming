"""This is a simple lifespan calculator"""
name = input("Enter your name: ").upper()
years_left = int(input("How many year do think you might live? "))
age = int(input("Pls, kindly enter your current age: "))

years_left = years_left - age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f" Dear {name}, you have {days_left} days,{weeks_left} weeks and {months_left} months left in this world!")