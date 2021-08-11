import random
num= random.randint(1, 10)  #Any random no B/W 1 to 10

print('Guess the number between 1 to 10 you have 3 chances; Good Luck!')
for _ in range(3):
    user_no = int(input('Guess the number: '))
    if user_no > num:
        print('Too far...')
    elif user_no < num:
        print('Too soon...')
    elif user_no==num:
        print("Yey!! you guessed right number, it's:", num)
        exit()
    else:
        print('Pls Try again')
