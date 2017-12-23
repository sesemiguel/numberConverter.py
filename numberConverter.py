#Created by Miguel Sese
import sys
def numberList():
    return "1-Decimal Input\n2-Hexadecimal Input\n3-Binary Input\n4-Octal Input\n5-Exit"

def errorDetected():
    return "Error Detected"

def decimalConversion(decimalNumber):
    hexNumber = hex(int(decimalNumber))
    binaryNumber = bin(int(decimalNumber))
    octalNumber = oct(int(decimalNumber))
    return "Hexadecimal: "+hexNumber+"\n"+"Binary: "+binaryNumber+"\n"+"Octal: "+octalNumber+"\n"

def hexadecimalConversion(hexadecimalNumber):
    decimalNumber = int(hexadecimalNumber, 16)
    binaryNumber = bin(decimalNumber)
    octalNumber = oct(decimalNumber)
    return "Decimal: "+str(decimalNumber)+"\n"+"Binary: "+binaryNumber+"\n"+"Octal: "+octalNumber+"\n"

def binaryConversion(binaryNumber):
    decimalNumber = int(binaryNumber, 2)
    hexadecimalNumber = hex(decimalNumber)
    octalNumber = oct(decimalNumber)
    return "Decimal: "+str(decimalNumber)+"\n"+"Hexadecimal: "+hexadecimalNumber+"\n"+"Octal: "+octalNumber+"\n"    

def octalConversion(octalNumber):
    decimalNumber = int(octalNumber, 8)
    binaryNumber = bin(decimalNumber)
    hexadecimalNumber = hex(decimalNumber)
    return "Decimal: "+str(decimalNumber)+"\n"+"Binary: "+binaryNumber+"\n"+"Hexadecimal: "+hexadecimalNumber+"\n"    

print("NUMBER CONVERTER PROGRAM")
print(numberList())
while True:

    numberInput = input("Enter desired input: ")
    
    if numberInput == '1':
        print("DECIMAL INPUT")
        try:
            decimalInput = input("Enter decimal input: ")
            print(decimalConversion(decimalInput))
        except ValueError:
            print(errorDetected())
        
    elif numberInput == '2':
        print("HEXADECIMAL INPUT")
        try:
            hexadecimalInput = input("Enter hexadecimal input: ")
            print(hexadecimalConversion(hexadecimalInput))
        except ValueError:
            print(errorDetected())
        
    elif numberInput == '3': 
        print("BINARY INPUT")
        try:
            binaryInput = input("Enter binary input: ")
            print(binaryConversion(binaryInput))     
        except ValueError:
            print(errorDetected())
        
    elif numberInput == '4':
        print("OCTAL INPUT")
        try:
            octalInput = input("Enter Octal input: ")
            print(octalConversion(octalInput))
        except ValueError:
            print(errorDetected())
        
    elif numberInput == '5':
        sys.exit("Exiting System")
        
    else:
        print(errorDetected())