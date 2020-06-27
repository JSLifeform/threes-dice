#threes dice game
from dice import Die, D6 



# initializes hand of dice
class Hand(list):
    def __init__(self, size = 5, die_type = D6, locked = False, *args, **kwargs):
        super().__init__()

        self.die_type = die_type
        self.size = size

        for _ in range(size):
            self.append(die_type())
        self.sort(key = threes_low)

# key function to sort list with locked dice then 3's at the beginning
def threes_low(item):
    if item.locked == True:
        return -1
    elif int(item) == 3:
        return 0
    else:
        return int(item)        

# checks to make sure user enters an integer from 1 to total number of unlocked dice
def check_int():
    while True:
        answer = input(f"How many dice would you like to keep this round? {kept_dice} kept currently.   ")
        try:
            answer = int(answer)
        except ValueError:
            print("Must enter an integer of at least 1.")
            # continue
        else:
            return answer

def lock_dice():
    # score = 0 <---deprecated, delete?
    for dice in range(0, kept_dice):
        h[dice].locked = True
        score += threes_low(dice.value)
    # return score <--- deprecated, delete?

# create hand and re/set kept dice to 0
h = Hand()
kept_dice = 0

#Begin game loop of keeping dice and re-rolling hand
while kept_dice < 5:
    
    while True:
        
        # prints dice to screen in loop
        for dice in h:
            # Below 3 lines in case I want 3's to be automatically kept?
            # if dice.value == 3:
            #     dice.locked = True
            #     kept_dice += 1
            if dice.locked == True:
                print(str(dice.value) + " KEPT")
            else: 
                print(dice.value)

        # checks that answer is integer
        answer = check_int()
        
        # checks that number of dice kept is 1 to total unkept dice
        if answer >= 1 and answer + kept_dice <= len(h):
            kept_dice += answer
            break
        elif kept_dice + answer > len(h):
            print(f"Too many dice! Only {len(h)} dice total!") 
            continue
        elif answer <= 1:
            print("Must keep at least 1 die per round.")
            continue

    # initialize score to be tallied in loop below
    score = 0
    # lock all dice user has decided to keep
    for _ in range(0, kept_dice):
        h[_].locked = True
        score = score + h[_].score
    #checks to see if game is over, prints current score if not
    if kept_dice < 5:   
        print(f"Your score is currently {score}")

    # removes all unkept dice
    del h[kept_dice: ]

    # add new dice to hand in place of unlocked dice
    for _ in range(kept_dice, h.size):
        h.append(h.die_type())

    # re-sort list
    h.sort(key = threes_low)

print(f"GAME OVER, man! Your final score is {score}")