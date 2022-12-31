import time
import webbrowser
import requests
import json

selection = ''
isint = ''

jokereq = (requests.get('https://official-joke-api.appspot.com/random_joke')).text

joke = json.loads(jokereq)

minesweepertable = [
    [
    ['|\n| 1 1 1\n|', [['Click the block closest to the wall',False], ['Click the block in the middle', False], ['Click the block 3rd closest to the wall',True]]],
    ['|\n| 1 2 1\n|', [['Click the block above the 2',False], ['Click the blocks above the ones',True], ['Click the one on the left and the top of the 2',False]]],
    ['|\n| 1 2 2 1\n|', [['Click the boxes above the ones',False], ['Click the first 2 and the last 1',False], ['Click both boxes above the ones', True]]]
    ], #beginner patterns
    [
        ['|     1\n| 1 1 1 1 1\n|', [['Click the boxes to the left and right of the top one', False], ['Flag the left and right boxes of the top one', False], ['click the boxes above the top one', True]]],
        ['|   2 1 3\n|     1\n 1 1 1 1 1\n|', [['click the boxes above the top 1', True], ['flag the boxes above the top 1', False], ['Flag the box above the top 1 and the box below 2', False]]]
    ], # Holes
    [

    ]
]


print('Welcome to my dictionary practice!')
time.sleep(2)
print('this project will help you memorize minesweeper patterns! (Keyword "Click" means space is free and "Flag" means flag a bomb)')
time.sleep(2)
while True:
    isint = ''
    selection = ''
    while not isint:
        print('What would you like to practice today?')
        print('1. Beginner Patterns  2. Holes')
        selection = input()
        isint = selection.isdigit()
        if isint and int(selection) > 2:
            isint = False
    selectionnum = int(selection)
    print('Loading '+str(len(minesweepertable)+1)+' questions!')
    time.sleep(1)
    for question in minesweepertable[selectionnum-1]:
        print('\n\n'+question[0])
        for num, answer in enumerate(question[1]):
            let = chr(ord('@')+(num+1))
            print(let+'. '+answer[0])
            if answer[1]:
                correctAnswer = [answer[0], let]
        ans = input('Put Letter Here!: ')
        if ans.upper() == correctAnswer[1].upper():
            print('\nCorrect! the answer is : '+correctAnswer[1]+'. '+correctAnswer[0])
        else:
            print('\nWrong! the correct answer is : '+correctAnswer[1]+'. '+correctAnswer[0])
    print('You have finished all the patterns! would you like to play again? (y/n)')
    playAgain = input()
    if playAgain.lower() == 'n':
        opentab = input('would you like to open the minesweeper.online pattern website? (y/n)')
        if opentab.lower() == 'y':
            webbrowser.open_new_tab('https://minesweeper.online/help/patterns')
            print('Goodbye!')
            time.sleep(2)
            exit()
        else:
            print('Goodbye!')
            print(joke['setup'])
            print('\n'+joke['punchline'])
            time.sleep(10)
            exit()

