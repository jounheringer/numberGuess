from random import randint
from time import sleep

# Set minimum and maximum value for range
mini = 1
maxi = 20
attempts = 0

# Chooses a random number between min and max
com = randint(mini, maxi)

# Ask for user's name
while True:
    name = str(input("\033[1;32mWhat's your name?? \033[m")).strip() 
    sleep(0.5)
    if name == '':
        print('\033[1;31mPlease type your name correctly\033[m')
    elif name.isnumeric():
        print('\033[1;31mPlease type your name correctly\033[m')
    else:
        break

#Tell how many attemps does the user have
print(f"\033[1;32m{name} you'll have 5 attempts to guess the number right\033[m")

# Take a number from the user and say if it's lower or higher based on the random number
while attempts < 6:
    while True:
        try:
            guess = int(input(f'\033[1;32mNow try to guess a number between {mini} and {maxi}: \033[m'))
            sleep(0.5)
        except:
            print('\033[1;31mPlease type an integer number \033[m')
        else:
            break
            print('')
    if guess == com:
        sleep(0.5)
        break
    if guess < com:
        print('\033[0;34mTry a little higher\033[m')
        sleep(0.5)
        attempts += 1
    if guess > com:
        print('\033[0;34mTyr a little lower\033[m')
        sleep(0.5)
        attempts += 1
    
if guess == com:
    print(f'\033[1;33mCongratulations, {name} you guessed the number in {attempts+1} attempts\033[m')

if guess != com:
    print(f'\033[1;35mYour attempts are over, the right number was {com}\033[m')

