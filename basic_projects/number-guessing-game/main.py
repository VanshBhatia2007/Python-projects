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



