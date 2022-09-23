########################################################################
##
## CS 101 Lab
## Program # 4
## Name Gregory Biskinis
## Email grbvpg@umsystem.edu
##
## PROBLEM : Describe the problem - I am simulating a slot machine system
##
## ALGORITHM : 
##      1. Get the users blanace
##      2. While the user has money
##      3. Get their wager
##      4. Get the slot results
##      5. Get the matches from the slot machine
##      6. Calculate the payouts
##      7. Add the users winnings to their bank
##      8. Print out the stats to the user stating things like matches, payouts, etc
##      9. Once the user is out of money, ask them if they would like to play again and if not, exit the program
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##      1. User doesnt enter a Y, Yes, N, or No: Keep asking
##      2. The wager isnt a valid value (greater than 0 and less than or equal to their total balance)
##      3. If the user doesn't enter a valid value for their bank balance (1-100), keep asking
##
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    playAgain = input('Do you want to play again?: ')

    if playAgain == 'Y' or playAgain == 'Yes':
        return True
    elif playAgain == 'N' or playAgain == 'No':
        return False
    else:
        playAgain = input('Must be Y, Yes, N, or No: ')





     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager = int(input('How much would you like to wager?: '))

    while wager <= 0 or wager >= bank:
        wager = int(input('Too high a value, you between 1 and your current bank account balance: '))

        
    return wager            






def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    intOne = random.randint(1, 10)
    intTwo = random.randint(1, 10)
    intThree = random.randint(1, 10)

    slot = (intOne, intTwo, intThree)

    return slot






def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''

    slots = get_slot_results()

    matches = 0

    if reela == slots[0]:
        matches += 1

    if reelb == slots[1]:
        matches += 1

    if reelc == slots[2]:
        matches += 1
        
    return matches

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    chips = int(input('How many chips would you like to play with?: '))

    while(chips <= 0 or chips >= 101):
        chips = int(input('You must choose a value between 1 and 100: '))


        
    return chips

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    payout = 0

    if(matches == 3):
        payout = wager * 10
    elif(matches == 2):
        payout = wager * 3
    elif(matches == 1):
        payout = wager
    elif(matches == 0):
        payout = wager * -1
        
    return payout   


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while(bank > 0):  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
