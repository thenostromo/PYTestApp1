import math

def isContinueIteration():
	back = input('\nGo back to the main menu? (y/n) ')
	continueIteration =(back == 'y')
	return continueIteration

while True:
    print("\nChoose the math operation.\n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")

    oper = input("\nYour option from the menu: ")


    if oper == "0" or oper == "1" or oper == "2" or oper == "3" or oper == "4":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

    #Addition
    if oper == "0":
        print("\nThe result is: " + str(val1 + val2) + "\n")

        if isContinueIteration():
            continue
        else:
            break

    #Subtraction
    elif oper == "1":
        print("\nThe result is: " + str(val1 - val2) + "\n")

        if isContinueIteration():
            continue
        else:
            break

    #Multiplication
    elif oper == "2":
        print("\nThe result is: " + str(val1 * val2) + "\n")

        if isContinueIteration():
            continue
        else:
            break

    #Division
    elif oper == "3":
        print("\nThe result is: " + str(val1 / val2) + "\n")

        if isContinueIteration():
            continue
        else:
            break

    #Modulo
    elif oper == "4":
        print("\nThe result is: " + str(val1 % val2) + "\n")

        if isContinueIteration():
            continue
        else:
            break

    #Raising to a power
    elif oper == "5":
        val1 = float(input("\nEnter the base: "))
        val2 = float(input("\nEnter the power: "))

        print("\nThe result is: " + str(math.pow(val1, val2)) + "\n")
        
        if isContinueIteration():
            continue
        else:
            break

    #Square root
    elif oper == "6":
        val1 = float(input("\nEnter value for extracting the square root: "))

        print("\nThe result is: " + str(math.sqrt(val1)) + "\n")

        if isContinueIteration():
            continue
        else:
            break
    
    #Logarithm
    elif oper == "7":
        val1 = float(input("\nEnter the value for calculating the logarithm to base 2: "))

        print("\nThe result is: " + str(math.log(val1, 2)) + "\n")

        if isContinueIteration():
            continue
        else:
            break
    
    #Sine
    elif oper == "8":
        val1 = float(input("\nEnter the value (in degrees) for calculating the sine: "))

        print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")

        if isContinueIteration():
            continue
        else:
            break

    #Cosine
    elif oper == "9":
        val1 = float(input("\nEnter the value (in degrees) for calculating the cosine: "))

        print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")

        if isContinueIteration():
            continue
        else:
            break

    #Tangent
    elif oper == "10":
        val1 = float(input("\nEnter the value (in degrees) for calculating the tangent: "))

        print("\nThe result is: " + str(math.tan(math.radians(val1))) + "\n")

        if isContinueIteration():
            continue
        else:
            break
    else:
        print("\nInvalid option!\n")
        continue
