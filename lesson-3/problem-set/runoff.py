# not sure what exact formula is wanted, i am going to use exaustive ballot

# getting an input number that is actually an integer
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return (userInput)

# getting a valid vote
def getValidChoice(choiceNumber,prevVotes):
    valid = False
    while valid == False:
        vote = input("Vote #"+str(choiceNumber)+": ")
        for p in candidateList:
            if vote == p:
                valid = True
                for z in prevVotes:
                    if vote != z:
                        pass
                    else:
                        print("You have already voted for them.")
                        valid = False
                        break                        
        if valid == False:
            print("Invalid, try again")
    return(vote)

# getting the candidates into a dictionary, in which the can be scored
candidates = {}
numOfCandidates = inputNumber("Enter the number of candidates: ")
for i in range(0,numOfCandidates):
    candidate = input("Input name of the candidate: ")
    candidates[candidate] = 0

# getting the number of voters
numOfVoters = inputNumber("Enter the number of voters: ")
print()
votes = []

# get the votes
candidateList = list(candidates.keys())
for i in range(0,numOfVoters):
    votes.append([])
    for p in range(0,numOfCandidates):
        votes[i].append(getValidChoice(p+1, votes[i]))
    print()

winner = ''
winnerFound = False

while True:

    # getting rid of all that are elim'd
    candidateList = list(candidates.keys())

    # setting score = to 0
    for i in range(0,len(candidates)):
        candidates[candidateList[i]] = 0

    # getting the top votes and setting the candidates score
    for i in range(0,len(votes)):
        candidates[votes[i][0]] += 1

    # seeing if someone has more than 50 percent
    for candidate in candidateList:
        if candidates[candidate] > numOfVoters / 2:
            winnerFound = True
            winner = candidate

    # breakcase
    if winnerFound:
        print("Winner:", winner)
        break

    # getting the biggest loser
    losers = []
    loserScore = -1
    for i in range(0,len(candidates)):
        if loserScore == -1:
            losers = []
            losers.append(candidateList[i])
            loserScore = candidates[candidateList[i]]
        elif candidates[candidateList[i]] < loserScore:
            losers = []
            losers.append(candidateList[i])
            loserScore = candidates[candidateList[i]]
        elif candidates[candidateList[i]] == loserScore:
            losers.append(candidateList[i])
            loserScore = candidates[candidateList[i]]

    # deleting the biggers loser(s)
    for loser in losers:
        for i in range(0,len(votes)):
            votes[i].remove(loser)
        del candidates[loser]

    if len(candidates) == 0:
        print("It was a tie")
        break