import random

string = ["Камінь", "Ножиці", "Папір"]

def num_part():
    while True:
        participation = input("Enter your number of participation (1 or 2): ")
        if participation in ["1", "2"]:
            return int(participation)
        else:
            print("Please try again.")

def user_choice():
    while True:
        user_choice = input("Choose: Камінь, Ножиці or Папір: ")
        if user_choice in string:
            return user_choice
        else:
            print("Please try again.")

def computer_choice():
    return random.choice(string)

def game():
    participation = num_part()
    userchoice = user_choice()
    computerchoice = computer_choice()
    print(f"Computer chose: {computerchoice}")
    if userchoice == computerchoice:
        print("Нічия!")
    elif (userchoice == "Камінь" and computerchoice == "Ножиці") or \
            (userchoice == "Ножиці" and computerchoice == "Папір") or \
            (userchoice == "Папір" and computerchoice == "Камінь"):
        print("Ви виграли!")
    else:
        print("Ви програли!")

game()














