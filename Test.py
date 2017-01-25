import random
import time

def BoredGame():
    print ("Made by Mark McCormick")
    names =  []
    name_1 = input ("Please sir can i have some more: ")
    name_2 = input ("Player 2 name: ")
    names.append(name_1)
    names.append(name_2)
    if names[0] == "":
        names[0] = "Player 1"
    if names[1] == "":
        names[1] = "Player 2"
    print ("")
    time.sleep(2)
    Player = {'Player_1': 0, 'Player_2':0}
    print (names[0], 'position:',  Player['Player_1'])
    print (names[1], 'position:',Player['Player_1'])
    print ("")


    while True:
        # Player 1 code
        print ('    ', names[0],':','    ')
        system = input ("Please press enter: ")
        P1_dice_one = random.randint (0, 6)
        P1_dice_two = random.randint (0, 6)
        print ("First dice:", P1_dice_one)
        time.sleep(1)
        print ("Second dice:", P1_dice_two)
        time.sleep(1)
        P1_score = P1_dice_one + P1_dice_two
        print ("You moved", P1_score, "places")
        time.sleep(1)
        Player['Player_1'] = P1_score + Player['Player_1']
        print ('Location:', Player['Player_1'])
        time.sleep(1)
        print("")
        # Player 1 if statement
        if Player['Player_1'] >= 24:
                print ("The Winner is...")
                time.sleep(2)
                print (names[0], '(Player 1)')
                time.sleep(1)
                break
        # Player 2 if code
        print ('      ', names[1],':')
        system = input ("Please press enter: ")
        P2_dice_one = random.randint (0, 6)
        P2_dice_two = random.randint (0,6)
        print ("First dice:", P2_dice_one)
        time.sleep(1)
        print ("Second dice:", P2_dice_two)
        time.sleep(1)
        P2_score = P2_dice_one + P2_dice_two
        print ("You moved", P2_score, "places")
        time.sleep(1)
        Player['Player_2'] = P2_score + Player['Player_2']
        print ('Location:', Player['Player_2'])
        time.sleep(2)
        print ("")
        # Player 2 if statement
        if Player['Player_2'] >= 24:
                print ("The Winner is...")
                time.sleep(2)
                print (names[1], '(Player 2)')
                break
# code to start or restart or leave
system_1 = input ("Do you want to start? ")
if system_1 == "yes" or system_1 == "Yes" or system_1 == 'ok' or system_1 == 'Ok':
    BoredGame()
elif system_1 == "no" or system_1 == "No" or system_1 == "no thank you":
    exit()
elif system_1 == "":
    BoredGame()
else:
    print ("Sorry but", system_1, "is not an answer")
    BoredGame()

system_2 = input ("Do you want to a rematch?")


if system_2 == 'yes' or system_2 == 'Yes':
     BoredGame()
elif system_2 == 'no' or system_2 == 'No':
    exit()
else:
    print ("Sorry but", system_2, "is not an answer")
    exit()
