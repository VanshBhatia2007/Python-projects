import random
number=random.randint(1,100)
while True:
    try:
        choice = int(input("guess the number :"))
        if choice > number :
            print("number is too high")
        elif choice < number:
            print("number is too low")
        else:
            print("congratulations you guessed the number")
            break
    except ValueError:
        print("invalid input")

# guess the number :20 
# number is too low
# guess the number :40
# guess the number :20
# number is too low
# guess the number :40
# number is too high
# guess the number :30
# number is too low
# guess the number :32
# number is too low
# guess the number :34
# number is too low
# guess the number :35
# number is too low
# guess the number :38
# number is too high
# guess the number :36
# number is too low
# guess the number :37
# congratulations you guessed the number





