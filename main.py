from encrypt import *
from decrypt import *
print("*" * 31)
print("Image Encryption and Decryption")
print("*" * 31)
print()

def getfilename () :
    print("Enter the filename, make sure the file is input directory.")
    filename = input()
    return filename
def reset() :
    def option() :
        print("Enter the id of the option to perform the specific task :-")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Quit")
        val = int(input())
        return val
    val = option()
    if val == 1 :
        encryption(getfilename())
    elif val == 2:
        decryption(getfilename())
    elif val == 3 :
        print("Thank you")
    else :
        print("****Please enter a valid option****")
    if val == 3 :
        exit(0)
    else :
        reset()
reset()