import random

def createRandomState (board_len):
    return [random.randint(0, board_len-1) for i in range (board_len)]

def createBoard (state):
    board = [[0] * len (state) ]
    for i in range (1,len (state)):
        board.append(board[i-1] [:])
    for i in range (len (state)):
        board[i] [state[i]] = 1
    return board

def calculateObjective (state):
    count = 0
    for i in range (len (state)):
        for j in range (i+1, len (state)):
            if state[j] == state[i] or state [5] == state[i] - i+j or state[j] == state[i] + i - j:
                count += 1
    return count

def getOptimalNeighbour (state):
    optimalState = state[:]
    optimalObjective = calculateObjective (state)
    for i in range (len (state)) :
        for j in range (len (state)):
            if state[i] != j:
                candidateState = state[:]
                candidateState[i] = j
                candidateObjective = calculateObjective (candidateState)
                if candidateObjective <= optimalObjective:
                    optimalObjective = candidateObjective
                    optimalState = candidateState[:]
    return (optimalObjective, optimalState)

def hillclimbing (state) :
        while True:
            objective, state = getOptimalNeighbour (state)
            print ('Objective: ', objective,'\tState: ', state)
            if objective == 0:
                return state
            else:
                state[random.randint(0, len (state)-1)] = random.randint (0,len (state)-1)

boardLen = int(input('Enter board length: '))
randomState = createRandomState (boardLen)
print ('Random board generated...')
print (randomState)
print (*createBoard (randomState), sep= '\n')
optimalState = hillclimbing(randomState)
print('Optimal board obtained...')
print (*createBoard (optimalState), sep = '\n')
print ('Optimal state: ', optimalState)