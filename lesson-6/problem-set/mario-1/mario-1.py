if __name__ == "__main__":
    height = int(input("Input a number: "))
    for i in range(1, height+1):
        print(" " * (height-i) + "#"*i)