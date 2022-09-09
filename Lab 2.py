#header to let the user know what program they are using
print('***** Welcome to the LAB grade calculator! *****')

#Gets input for the student name and stores it in a string variable
name = input('Who are we calculating grades for? -->\n')

#Gets input for the students labs grade and stores in into an integer variable
labGrade = int(input('What is their Labs grade? -->\n'))

#checks to make sure the lab grade meets the guidelines (less than 100 but more than 0)
#and if it does not, it lets the user know and adjusts the grade to the appropriate value
if(labGrade > 100):
    print('The lab value should have been 100 or less. It has been changed to 100')
    labGrade = 100
elif(labGrade < 0)
    print('The lab value should have been 0 or more. It has been changed to 0')
    labGrade = 0  


#Gets input for the students exams grade and stores in into an integer variable
examGrade = int(input('What is their Exams grade? -->\n'))

#checks to make sure the exams grade meets the guidelines (less than 100 but more than 0)
#and if it does not, it lets the user know and adjusts the grade to the appropriate value
if(examGrade > 100):
    print('The exam value should have been 100 or less. It has been changed to 100')
    examGrade = 100
elif(examGrade < 0):
    print('The exam value should have been 0 or more. It has been changed to 0')
    examGrade = 0  

#Gets input for the students attendance grade and stores in into an integer variable
attGrade = int(input('What is their Attendance grade? -->\n'))

#checks to make sure the attendance grade meets the guidelines (less than 100 but more than 0)
#and if it does not, it lets the user know and adjusts the grade to the appropriate value
if(attGrade > 100):
    print('The attendance value should have been 100 or less. It has been changed to 100')
    attGrade = 100
elif(attGrade < 0):
    print('The attendance value should have been 0 or more. It has been changed to 0')
    attGrade = 0  

#Calculates the weighted grade by adding the students grades times the weight value
#and stores it into a floating point variable because this value can be a decimal
weightGrade = (labGrade * 0.7) + (examGrade * 0.2) + (attGrade * 0.1)

#initializes the letter grade variable and sets it to an empty value for now
letterGrade = ''

#Performs the check to determine what letter grade the student got based on their
#weighted grade (90+ = A, 80-89 = B, 70-79 = C, 60-69 = D, and 60 or lower is an F)
if(weightGrade >= 90.0):
    letterGrade = 'A'
elif(weightGrade >= 80 and weightGrade <= 89):
    letterGrade = 'B'
elif(weightGrade >= 70 and weightGrade <= 79):
    letterGrade = 'C'
elif(weightGrade >= 60 and weightGrade <= 69):
    letterGrade = 'D'
else:
    letterGrade = 'F'

#prints out the students weighted grade to the user
print(f'The weighted grade for {name} is {weightGrade}')

#prints out the students letter grade to the user
print(f'{name} has a letter grade of {letterGrade}')

#prints out a closing statement to let the user know they are finished
print('***** Thanks for using the Lab grade calculator *****')
