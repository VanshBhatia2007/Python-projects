import random
import string

length = int(input("Enter the length of password: "))

print('''choose the character set for password :
                  1. numbers
                  2. letters
                  3. special characters
                  4. exit''')

ch_list = ""

while (True):
    choice = int(input("Pick a number "))
    if (choice == 1):
        ch_list +=string.digits
    elif (choice == 2):
        ch_list +=string.ascii_letters
    elif (choice == 3):
        ch_list += string.punctuation
    elif (choice == 4):
        break
    else:
        print("pick a valid number")

password = []
for i in range(length):
    randomchar = random.choice(ch_list)
    password.append(randomchar)

print("The random password is " + "".join(password))

# output :
# Enter the length of password: 10
# choose the character set for password :
#                   1. numbers
#                   2. letters
#                   3. special characters
#                   4. exit
# Pick a number 1
# Pick a number 2
# Pick a number 3
# Pick a number 4
# The random password is ]AlN3Z'7I@