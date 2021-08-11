import random

length = int(input('Enter lengh of password: '))
a = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
print('Your password suggestion are: ')
for i in range(1, 4):
    # Sample take list, string,etc and size & returns random nos from that list/string in [list format] with len=size
    b = random.sample(a, length)
    # Here a= string, size= length
    password = "".join(b)  # Joins concat "" and b
    print(i, ':', password)
