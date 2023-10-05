def doorNumbers(start, end, problem_numbers): #define a function called doorNumbers that counts numbers containing a digit, or digits, within a given range
    count = 0 #counter to keep track of the count of numbers containing specified digit, or digits
    for number in range(start, end + 1): #looks through each number in the range specified
        for char in str(number): #check if the specified digit is present in the current numerical string
            if char in problem_numbers:
                count += 1 #increment the count if the digit is found in the number
    return count #return the final count of numbers containing the digits specified

#define the range of numbers to look through which contain the digit specified
start_range = 1
end_range = 1150
problem_numbers = input("Please enter both digits for manufacturing issue, separating digits with a comma: ")
problem_numbers = problem_numbers.replace(" ", "").split(",")

count = doorNumbers(start_range, end_range, problem_numbers) #calls the doorNumbers function with the specified range and gets the count of digits specified
print(f"Number of doors containing the digits 6 and 9 in the range 1-1150 that need replaced: {count}") #prints the result, showing how many numbers contain the specified digit in the specified range

#Result = 650. Both 6 and 9's equal 325 needed for the total number of rooms, therefore 650 would be needed for both