ip = input('Enter a string with numbers: ')
search = input('Enter the number you want to search in the string: ')

# for i in ip: --->My mistake
for i in range(len(ip)):
    if search == ip[i]:
        print('The number is found at: ', ip[i])
        quit()

print('Number not found')


"""
if search == ip[1]:
    print('Hii')
"""