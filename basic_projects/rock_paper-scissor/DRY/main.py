import random
Rock = "r"
Scissors = "s"
Paper = "p"
d={"Rock" : "🪨" , "Paper" : "📃" , "Scissors" : "✂️"}
choices = tuple(d.Keys())

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
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")):
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
# rock , paper , scissors (r/s/p):r
 # you choose 🪨
# computer choose 🪨
# Tie
# wanna continue ?(y/n)y
# rock , paper , scissors (r/p/s):s
# you choose ✂️
# computer choose 📃
# you win
# wanna continue ?(y/n)n
 
