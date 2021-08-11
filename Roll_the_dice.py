import random

while True:
    print(""" What do you want to do?
            1. Roll the dice
            2. Stop """)
    no= int(input())
    if no == 1:
        print(random.randint(1,6))
    else:
        print('Stopping rolling the dice....')
        break
