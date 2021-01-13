def getValidInput():
    result = ''
    while True:
        result = input("Please input key number: ")
        if result.isdigit():
            result = int(result)
            if result > 0 and result < 26:
                break
    return (int(result))

key = getValidInput()
plainText = input("Plain Text: ")

cipherText = ""
for i in range(0,len(plainText)):
    if plainText[i].isupper():
        letterIndex = ord(plainText[i]) + key
        if letterIndex > 90:
            letterIndex -= 26
        cipherText += chr(letterIndex)
    elif plainText[i].islower():
        letterIndex = ord(plainText[i]) + key
        if letterIndex > 122:
            letterIndex -= 26
        cipherText += chr(letterIndex)
    else:
        cipherText += plainText[i]

print("CipherText:",cipherText)