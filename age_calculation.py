import datetime
#library

name = input("What is your name? ")

#name variable controls input for name

age = int(input("What is your age? "))

#age variable controls input for age with an integer prior to the input

current_year = datetime.datetime.now().year

#current_year variable gets the current date and time from the datetime.datetime.now function and the .year variable

year_of_100 = current_year + 100 - age

#adds 100 to the current_year variable and then subtracts users age to gather what year they will turn 100

print(f"Hi {name}, you will turn 100 years old in the year {year_of_100}")

#outputs the result