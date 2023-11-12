# program for an implementation of the popular rock, paper, scissors game

import random

userPoints = 0
opponentPoints = 0

#main game logic
def rps():
    moveStr = ''
    moveNum = -1
    
    def inputMove():
        moveNum = input('Enter 1, 2 or 3 for rock, paper or scissors: ')
        while not moveNum.isdigit():
            print("Invalid input, try again")
            moveNum = input('Enter 1, 2 or 3 for rock, paper or scissors: ')
        moveNum = int(moveNum)
        
    inputMove()
    opMove = random.randint(1, 3)
     
    if moveNum == 1:
        if opMove == 1:
            return 'draw'
        elif opMove == 2:
            return 'loss'
        else:
            return 'win'
    elif moveNum ==2:
        if opMove == 1:
            return 'win'
        elif opMove == 2:
            return 'draw'
        else:
            return 'loss'
    else:
        if opMove == 1:
            return 'loss'
        elif opMove == 2:
            return 'win'
        else:
            return 'draw'
      
while True:
    result = rps()
    if result == 'win':
        print('You won! :)')
        userPoints += 1
    elif result == 'loss':
        print('You lost :(')
        opponentPoints += 1
    else:
        print('Draw!')
    
    # prints game scores after each round
    print('Player score: ' + str(userPoints))
    print('Opponent score: ' + str(opponentPoints))
    
    # ask user if they want to continue and break if not
    if input('Do you want to continue ? (y/n)') != 'y':
        print('Goodbye!')
        break