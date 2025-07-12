import random 
d={"r" : "🪨" , "p" : "📃" , "s" : "✂️"}
choices = ("r","p","s")

def get_choices():
    while True:
        user_choice = input("rock , paper , scissors (r/p/s):").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("invalid choice")
            
def display_choices(user_choice,computer_choice):
    print(f"you choose {d[user_choice]}")
    print(f"computer choose {d[computer_choice]}")

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        print("Tie")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")):
        print("you win")
    else:
        print("you lose")
def play_game():
    while True:
        user_choice = get_choices()
        computer_choice = random.choice(choices)
        display_choices(user_choice,computer_choice)
        determine_winner(user_choice,computer_choice)

        continue_c = input("wanna continue ?(y/n)").lower()
        if continue_c == "n":
            break

play_game()

# ouput :
# rock , paper , scissors (r/p/s):r
 # you choose 🪨
# computer choose 🪨
# Tie
# wanna continue ?(y/n)y
# rock , paper , scissors (r/p/s):s
# you choose ✂️
# computer choose 📃
# you win
# wanna continue ?(y/n)n
 
