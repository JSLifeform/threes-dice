#threes dice game
from dice import Die, D6 




class Hand(list):
    def __init__(self, size = 5, die_type = D6, locked = False, *args, **kwargs):
        super().__init__()

        for _ in range(size):
            self.append(die_type())
        self.sort(key = threes_low)

# key function to sort list with 3's at the beginning
def threes_low(item):
    if int(item) == 3:
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



h = Hand()
kept_dice = 0

while kept_dice < 5:

    for dice in h:
        print(dice.value)
        # if dice.value == 3:
        #     dice.locked = True
        #     kept_dice += 1
        print(dice.locked)
        

    answer = check_int()
    if answer >= 1 and answer + kept_dice <= len(h):
        kept_dice += answer
    elif kept_dice + answer > len(h):
        print(f"Too many dice! Only {len(h)} dice total!") 
    elif answer <= 1:
        print("Must keep at least 1 die per round.")


    for _ in range(0, kept_dice):
        h[_].locked = True
