"""
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program
"""
def encode(message):
    list = ""
    count = 1
    if(len(message) == 1):
        list = list + str(count)+message
    else:
        for i in range(len(message)-1):
            if(message[i] == message[i+1]):
                count = count+1
            else:
                list = list + str(count) + message[i]
                i = i+1
                count = 1


        list = list + str(count) + message[i]

    return list
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("MAAKKAJ")
print(encoded_message)
