
#Variable to control when the game starts and ends
yes_no = 'y'

#Variable to hold the computers guess for the number
the_num = 0

#While the user wants to continue playing
while(yes_no == 'y'):

    #Asks the user to think of a number in their head but not input it into the computer
    print('Please think of a number between and including 1 and 100.')

    #Variable to hold the remainder when the users number is divided by 3
    rem_div_3 = int(input('What is the remainder when your number is divided by 3?: '))

    #While the input is invalid
    while(rem_div_3 < 0 or rem_div_3 >= 3):
        print('The remainder must be 0, 1, or 2')
        rem_div_3 = int(input('What is the remainder when your number is divided by 3?: '))

    #Variable to hold the remainder when the users number is divided by 5
    rem_div_5 = int(input('What is the remainder when your number is divided by 5?: '))

    #Variable to hold the remainder when ht users number is divided by 5
    rem_div_7 = int(input('What is the remainder when your number is divided by 7?: '))

    #Iterate through a list of values 1 to 100 to figure out the users number
    for x in range(1, 101):

        #If the current number in the iteration of 1-100 has the same remainders for 3, 5, and 7
        #As the users inputs for those values, then their number is the current iteration
        if(x % 3 == rem_div_3 and x % 5 == rem_div_5 and x % 7 == rem_div_7):
            the_num = x

            #Exit the loop
            break

    #Print out what the users number is
    print(f'Your number was {x}')
    print('How amazing is that?')

    #Asks if the user wants to play again, if they put in Y then the game starts again
    yes_no = input('Do you want to play again?: Y to continue, N to quit: ')

    #While the user doesn't enter a valid value, just keep asking them
    while(yes_no != 'y' and yes_no != 'n'):
        yes_no = input('Do you want to play again?: Y to continue, N to quit: ')
