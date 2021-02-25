class hashTable:
    def __init__(self, len = 100):
        self.max = len
        # setting 100 values to an array
        self.arr = [[] for i in range(self.max)]

    def getHash(self, key):
        h = 0
        for character in key:
            h += ord(character)
        return(h % self.max)
    
    def __setitem__(self, key, value):
        h = self.getHash(key)

        for i in range(0,len(self.arr[h])):
            if self.arr[h][i][0] == key:
                self.arr[h][i] = [key, value]
                return
        self.arr[h].append([key, value])

    def __getitem__(self, key):
        h = self.getHash(key)

        for i in self.arr[h]:
            if i[0] == key:
                return(i[1])
        return(None)

    # def __delitem__(self, key):
    #     h = self.getHash(key)

    #     for i in range(0,len(self.arr[h])):
    #         if self.arr[h][i][0] == key:
    #             self.arr[h].pop(i)
    #             return

def isValidWord(hashTable, word):
    value = hashTable[word]
    if value:
        return True
    return False

def getString(message = "Input a string: "):
    userInput = str(input(message))
    return(userInput)

def getWords(strr): 
    word = strr.split(" ") 
    words = [*word]
    # removes all the nonalpha chars
    for index, myWord in enumerate(words):
        tmp = ''.join(c for c in myWord if c.isalpha())
        words[index] = tmp
    return(words)

if __name__ == "__main__":

    table = hashTable(1000)

    words = open("message.txt", "r")
    lines = words.readlines()

    for line in lines:
        # strip removes the newline char
        table[line.strip()] = True


    while True:
        myInput = getString()
        if myInput == "quit" or myInput == 0:
            break
        words = getWords(myInput)
        invalidWords = []
        for word in words:
            word = word.lower()
            if isValidWord(table, word):
                pass
            else:
                invalidWords.append(word)
    
        print(invalidWords)
        print("Number of mispelled words:", len(invalidWords))