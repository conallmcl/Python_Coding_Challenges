def doorNumbers(start, end): #define a function called doorNumbers that counts numbers containing a digit, or digits, within a given range
    count = 0 #counter to keep track of the count of numbers containing specified digit, or digits
    for number in range(start, end + 1): #looks through each number in the range specified
        if '6' in str(number): #check if the specified digit is present in the current numerical string
            count += 1 #increment the count if the digit is found in the number
        if '9' in str(number): #check if the specified digit is present in the current numerical string
            count += 1 #increment the count if the digit is found in the number
    return count #return the final count of numbers containing the digits specified

#define the range of numbers to look through which contain the digit specified
start_range = 1
end_range = 1150

count = doorNumbers(start_range, end_range) #calls the doorNumbers function with the specified range and gets the count of digits specified
print(f"Number of doors containing the digits 6 and 9 in the range of 1 to 1150: {count}") #prints the result, showing how many numbers contain the specified digit in the specified range