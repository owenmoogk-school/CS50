def getValidInput():
    result = ''
    while True:
        result = input("Enter height:")
        if result.isdigit():
            break
    return (int(result))

height = getValidInput()

print ("Height: ", height)
height += 1

for row in range(0,height):
    print ((" " * (height - row)), "#" * row, " ", "#" * row)