"""
Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers.
Note: Assume that all the numbers are two digit numbers.
"""
#lex_auth_01269441913243238467

def create_largest_number(number_list):
    largest = 0 
    number_list.sort()
    for i in range(0,len(number_list)):
        largest = largest + (number_list[i] * pow(100,i))
    
    return largest
    
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
