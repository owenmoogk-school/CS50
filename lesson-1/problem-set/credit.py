def getValidInput():
    result = ''
    while True:
        print("Enter a credit card number (totally not illegal): ")
        result = input()
        if result.isdigit():
            break
        else:
            pass
    return (int(result))

def isValid(number):
    number = str(number)

    if len(number) < 13 or len(number) > 16:
        return(False)
    else:
        digits = []
        for i in range (0,len(number),2):
            digits.append(int(number[i])*2)
        total = 0
        for i in range (0,len(digits)):
            num = digits[i]
            num = str(num)
            for i in range (0,len(num)):
                total += int(num[i])
        for i in range (1, len(number), 2):
            total += int(number[i])
        if total%10 == 0:
            return(True)
        else:
            return(False)

def getType(number):
    number = str(number)
    if number[0] == '3':
        return("AMEX")
    elif number[0] == '4':
        return("VISA")
    elif number[0] == '5':
        return("MASTERCARD")
    else:
        return("UNRECOGNIZED")

number = getValidInput()
if isValid(number):
    print(getType(number))
else:
    print("INVALID")