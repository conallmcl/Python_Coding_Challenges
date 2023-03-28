import numbers
#library

def Split(decimals):
    even_li = []
    odd_li = []
    for i in decimals:
        if (i % 2 == 0):
            even_li.append(i)
        else:
            odd_li.append(i)
    print("Even numbers: ", even_li)
    print("Odd numbers: ", odd_li)

#defined Split function splits the even_li and odd_li variables into arrays, the decimals are sorted based on whether the number is divisible by 2, if not it is sorted into the odd number list

decimals = list()

#decimals variable defined into list function

n=int(input("Enter the size of the First List ::"))
print("Enter the Element of First  List ::")
for i in range(int(n)):
   k=int(input(""))
   decimals.append(k)
Split(decimals)

#driver code that allows user to enter the size of the list of decimals they'd like to enter, and then asks them to enter the decimals. Upon finishing entry, automatically sorts digits into even and odd lists