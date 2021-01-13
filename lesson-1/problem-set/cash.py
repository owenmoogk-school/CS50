def getValidInput():
    valid = False
    while valid == False:
        change = input("Enter the change due: ")
        try:
            change = float(change)
        except:
            print("Try again.")
        else:
            valid = True
    return(change)

change = getValidInput()

change = change * 100 # get cents
print(change)
coins = 0

while change != 0:
    if change >= 25:
        coins += 1
        change -= 25
    elif change >= 10:
        coins += 1
        change -= 10
    elif change >= 5:
        coins += 1
        change -= 5
    elif change >= 1:
        coins += 1
        change -= 1

print("You need", coins, "coins.")