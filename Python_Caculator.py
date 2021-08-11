def add(a, b) :
    return a+b

def sub(a, b):
    return a - b

def Div(a, b):
    return a / b

def multi(a, b):
    return a * b


no1, no2 = 15, 30

print(""" Enter following number for perfoming calculation:
      0: add
      1: sub
      2: multi
      3: Div 
      **Other nos won't work** """)

x= int(input('Enter your choice: '))

if x==0:
    addition = add(no1, no2)
    print(addition)
if x==1:
    subtraction = sub(no1, no2)
    print(subtraction)
if x==2:
    multiplication = multi(no1, no2)
    print(multiplication)
if x==3:
    Division = Div(no1, no2)
    print(Division)
