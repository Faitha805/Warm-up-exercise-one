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
        account_balance -= withdraw_amount
        print("You have successfully withdrawn {withdraw_amount}. Your new account balance is {account_balance}")

elif student_option ==3:
    print(f"Your account balance is {account_balance}")

else :
    print("You've entered a wrong choice, please enter 1, 2 or 3.")
            
    run = int(input("To continue, enter 1. To exit, enter any other number."))
    
    if run!= 1:
        print("Thank you for using our WITI Academy Sacco")
        break