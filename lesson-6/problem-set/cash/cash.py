if __name__ == "__main__":
    owed = float(input("Change Owed: "))
    owed = int(owed * 100)

    currNum = 0
    while owed > 0:
        if owed >= 25:
            owed -= 25
        elif owed >= 10:
            owed -= 10
        elif owed >= 5:
            owed -= 5
        elif owed >= 1:
            owed -= 1
        currNum += 1

    print(currNum)