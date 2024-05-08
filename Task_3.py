"""
Task- 03
Rock-paper-sisor
"""

import random
print('\nWelcome to ROCK PAPER SCISSOR GAME\nYou will get "5" chances in Each round, you ca play as many round you want')
ls = ['R', 'P', 'S']
i = 1

while 1:
    print("\nRound: ", i, "\n")
    for j in range(5):
        rs = random.choice(ls)
        print("Enter  R: ROCK  P: PAPER  S: SCISSOR")
        ui = input("Enter Your Choice: ")
        print("Computer choice: ", rs)
        if (ui == 'R' and rs == 'R'):
            print("Tie")
        elif (ui == 'R' and rs == 'S'):
            print("Win")
        elif (ui == 'R' and rs == 'P'):
            print("Loose")
        elif (ui == 'P' and rs == 'P'):
            print("Tie")
        elif (ui == 'P' and rs == 'R'):
            print("Win")
        elif (ui == 'P' and rs == 'S'):
            print("Loose")
        elif (ui == 'S' and rs == 'S'):
            print("Tie")
        elif (ui == 'S' and rs == 'P'):
            print("Win")
        elif (ui == 'S' and rs == 'R'):
            print("Loose")
    i = i + 1
    cont = int(input("Do you want to continue for the next round:\nEnter 1 to continue else 0: "))
    if (cont == 0):
        break
print ("\nThank you for playing this game.")
