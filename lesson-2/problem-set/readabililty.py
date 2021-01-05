def findWords(text):
    spaces = 1
    for i in text:
        if i == " ":
            spaces += 1
    return (spaces)

def findSentences(text):
    sentences = 1 # starting at one because the last one wont be counted. (since there is no space)
    for i in range (0, len(text)-1):
        if text[i].isalpha() == False and text[i+1] == " " and text[i+2].isupper() == True:
            sentences += 1
    return(sentences)

def findLetters(text):
    letters = 0
    for i in text:
        if i.isalpha():
            letters += 1
    return(letters)

print("Please input the text.")
text = input()

words = findWords(text)
sentences = findSentences(text)
letters = findLetters(text)

l = letters / words * 100
s = sentences / words * 100

grade = (0.0588*l) - (0.296 * s) - 15.8
print (round(grade))