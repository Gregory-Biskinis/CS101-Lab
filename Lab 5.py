import string

#Function takes a string variable and gets the value of the school that the student is enrolled in by checking the value at index 5 of the given string and returns the school
def get_school(card):
    
    if card[5] == "1":
        return "School of Computing and Engineering"
    elif card[5] == "2":
        return "School of Law"
    elif card[5] == "3":
        return "College of Arts and Sciences"
    else:
        return "Invalid School"

#Function takes a string variable and gets the value of the grade that the student is in by checking the value at the index 6 and returns the grade
def get_grade(card):

    num = int(card[6])
    
    if num == 1:
        return "Freshman"
    elif num == 2:
        return "Sophomore"
    elif num == 3:
        return "Junior"
    elif num == 4:
        return "Senior"
    else:
        return "Invalid Grade"

#Function gets the value of a character by checking its value in the alphabet (ie; A=1, B=2, etc.) and returns the value
def character_value(character):
    return string.ascii_uppercase.index(character)

#Function gets the check digit of the card by taking each value in the string and getting its value (A=1, B=2, etc) and multiplying it by the index plus 1, then taking its remainder when divided by 10
#And returns that value
def get_check_digit(card):
    check_digit = 0
    counter = 0
    for i in card:
        if i.isdigit():  
            check_digit += (counter + 1) * int(i)
            counter += 1
        else:
            check_digit += (counter + 1) * character_value(i)
            counter += 1

    check_digit = check_digit % 10
    return check_digit

#Function takes the card value and runs it through a series of tests to make sure the card is valid
def verify_check_digit(card):

    return_value = ()
    counter = 0
    
    if len(card) != 10:
        return_value = (False, "The length of the number given must be 10")
        return return_value

    for i in card[0:5]:
        if i.isdigit():
            return_value = (False, f"The first 5 characters must be A-Z, the invalid character is at {counter} is {i}")
            return return_value
        counter += 1

    counter = 0
    for i in card[7:10]:
        if i.isdigit() == False:
            return_value = (False, f"The last 3 characters must be 0-9, the invalid character is at {counter} is {i}")
            return return_value
        counter += 1

    
    if card[5] != '1' and card[5] != '2' and card[5] != '3':
        return_value = (False, "The sixth character must be 1 2 or 3")
        return return_value

    if card[6] != '1' and card[6] != '2' and card[6] != '3' and card[6] != '4':
        return_value = (False, "The seventh character must be 1 2 3 or 4")
        return return_value

    if card[9] != get_check_digit(card):
        return_value = (False, f"Check Digit {card[9]} does not match calculated value {get_check_digit(card)}.")
        return return_value

    return (True, "")


#Gets input for the card from the user      
card = input("Enter Library Card. Hit Enter to Exit ==> ")


#While the user puts a value in for the card
while(card != ""):

    #Verify the card and store the results in a list
    results = verify_check_digit(card)

    #If the card passes the tests
    if results == (True, ""):

        #Print that the card is valid
        print("Library Card is Valid")

        #Print what school the student who the card belongs to is in
        print(f"The card belongs to a student in {get_school(card)}")

        #Print the grade the student who the card belongs to is in
        print(f"The card belongs to a {get_grade(card)}")

    #If the card is not valid
    else:
        #Print out what the problem is
        print(results[1])

    #Get a new value for the library card and if empyty, exits the loop
    card = input("Enter Library Card. Hit Enter to Exit ==> ")

