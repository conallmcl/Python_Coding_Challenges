import numbers
#library

name = input("Hi, what is your name? ")
first_decimal = int(input("Please enter a decimal: "))
second_decimal = int(input("Please enter another decimal: "))

#name variable controls name input
#first_decimal and second_decimal control number inputs via integer function

sum = first_decimal + second_decimal
difference = first_decimal - second_decimal
product = first_decimal * second_decimal
quotient = first_decimal / second_decimal

#sum gathered by adding first_decimal and second_decimal
#difference gathered by subtracting first_decimal and second_decimal
#product gathered by multiplying first_decimal and second_decimal
#quotient gathered by dividing first_decimal and second_decimal

print(f"Hi {name}, the sum of your query is {sum}. The difference is {difference}. The product is {product}. Finally, the quotient is {quotient}. Have a good day!")

#outputs result