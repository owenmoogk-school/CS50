def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return (userInput)

candidates = {}
numOfCandidates = inputNumber("Enter the number of candidates: ")

for i in range(0,numOfCandidates):
    candidate = input("Input a name of the candidate: ")
    candidates[candidate] = 0

numOfVoters = inputNumber("Enter the number of voters: ")

candidateList = list(candidates.keys())
for i in range(0,numOfVoters):
    valid = False
    while valid == False:
        vote = input("Vote: ")
        for p in candidateList:
            if vote == p:
                valid = True
                candidates[vote] += 1
        if valid == False:
            print("Invalid, try again")

winners = []
highscore = 1 # there must be at least one vote to at least one candidate
for i in range(0,len(candidates)):
    if candidates[candidateList[i]] > highscore:
        winners = []
        winners.append(candidateList[i])
        highscore = candidates[candidateList[i]]
    elif candidates[candidateList[i]] == highscore:
        winners.append(candidateList[i])

print("WINNERS: ")
for i in winners:
    print (i)