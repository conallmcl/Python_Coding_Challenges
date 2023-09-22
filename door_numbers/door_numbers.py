def doorNumbers(start, end): #define a function called doorNumbers that counts numbers containing the digit 7 within a given range
    count = 0 #counter to keep track of the count of numbers containing 7
    for number in range(start, end + 1): #looks through each number in the range specified
        if '7' in str(number): #check if the digit 7 is present in the current numerical string
            count += 1 #increment the count if the digit 7 is found in the number
    return count #return the final count of numbers containing the digit 7

#define the range of numbers to look through which contain the digit 7, in this case 1 through 250
start_range = 1
end_range = 250

count = doorNumbers(start_range, end_range) #calls the doorNumbers function with the specified range and gets the count of digits with 7
print(f"Number of doors containing the digit 7 in the range of 1 to 250: {count}") #prints the result, showing how many numbers contain 7 in a range of 1 through 250, in this case 43 being the result