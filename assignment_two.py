#1
# The volume of a sphere with radius r is (4/3)* pie * r**2. 
# What is the volume of the sphere with radius 5. 
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places


radius = int(input("Enter the radius of the sphere: "))
#import math library
import math
volume_of_the_sphere = (4/3)*math.pi*(radius**3)
print(f"The volume of the sphere with a radius {radius} is {volume_of_the_sphere:.2f}")

#2
# Create a program to calculate the area of a triangle (1/2 * base * height). 
# Base and height should be entered using the keyboard. 


base = int(input("Enter the length of the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area = ((1/2) * base * height)
print(f"The area of the triangle with a base of {base} and height of {height} is: {area} ")

#3
# WITI has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving based on the mark scored in a subject. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89%   Grade is  B
# 70% - 79%   Grade is C                                                        
# 60% - 69%   Grade is D                  
# 50% - 59%   Grade is E  
# < 50% Fail 


print("Grading Student's Mark")
#Entry of students marks
mark_scored = int(input("Enter the mark scored: "))

#Grading a students mark
if 90 <= mark_scored <= 100 :
    print("Grade is A")

elif 80 <= mark_scored <= 89 :
    print("Grade is B")

elif 70 <= mark_scored <= 79 :
    print("Grade is C")

elif 60 <= mark_scored <= 69 :
    print("Grade is D")

elif 50 <= mark_scored <= 59 :
    print("Grade is E")

else :
    print("Fail") 



#4
#  WITI Academy is proposing a Sacco to help students save their money. 
#  Design a platform that will do the following.
#  Welcome to, WITIAcademy Sacco.
#  1. Deposit Money
#  2. Withdraw Money
#  3. Check Balance
#  Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#  If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
#  If the student selects 3, the account balance should be displayed.


account_balance = 0
run = 1

while run == 1:
    print(" Welcome to, WITIAcademy Sacco.")
    #menu
    print(" 1. Deposit Money")
    print(" 2. Withdraw Money")        
    print(" 3. Check Balance")

student_option = int(input("Enter your selection (1,2 or 3): "))

#performing transaction based on the student's choice
if student_option == 1:
    print("Depositing Money...")

    deposit_amount = int(input("Enter amount of money to be deposited: "))
    #Since deposit amount should be >1000
    if deposit_amount < 1000 :
        print("The minimum amount to deposit is 1000")

    else :
        account_balance += deposit_amount
        print(f"You have successfully deposited {deposit_amount}, your new account balance is {account_balance}.")

elif student_option ==2:
    print("Withdrawing Money...")

    withdraw_amount = int(input("Enter amount of money to be deposited: "))
    if account_balance == 0:
        print("Your account balance is 0")

    elif withdraw_amount < 500:
        print("The minimum amount of money to withdraw is 500.")

    elif withdraw_amount > account_balance:
        print("You do not have sufficient funds to complete  this task.")

    else :
        account_balance -= deposit_amount
        print("You have successfully withdrawn {withdraw_amount}. Your new account balance is {account_balance}")

elif student_option ==3:
    print(f"Your account balance is {account_balance}")

else :
    print("You've entered a wrong choice, please enter 1, 2 or 3.")
            
run = int(input("To continue, enter 1. To exit, enter any other number."))
if run!= 1:
    print("Thank you for using our WITI Academy Sacco")
    break
