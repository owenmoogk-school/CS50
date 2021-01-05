correctKey = False
key = ""
while correctKey == False:
    print ("Enter a key:")
    key = str(input())
    improper = False
    if len(key) == 26:
        for i in key:
            if i.isalpha():
                pass
            else:
                improper = True
                break
    else:
        improper = True

    if improper:
        continue
    else:
        break

key = key.upper()

print("Plain Text:")
plainText = input()
cipherText = ""

for i in range(0,len(plainText)):
    if plainText[i].isupper():
        letterIndex = ord(plainText[i]) - 65
        cipherText += key[letterIndex]
    elif plainText[i].islower():
        letterIndex = ord(plainText[i]) - 97
        cipherText += key[letterIndex].lower()
    else:
        cipherText += plainText[i]

print(cipherText)