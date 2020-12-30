def getValidInput():
    result = ''
    while True:
        print("Enter height:")
        result = input()
        if result.isdigit():
            break
        else:
            pass
    return (int(result))


height = getValidInput()

print ("Height: ", height)
height += 1

for row in range(0,height):
    print ((" " * (height - row)), "#" * row, " ", "#" * row)