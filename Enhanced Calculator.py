#Calculator with Scientific Additions
#Credits john-geo-coding
from math import *

#Addition
def addition():
    x1=float(input("Type the first number:"))
    x2=float(input("Type the second number:"))
    print("Your sum is:")
    print( x1+x2 )

#Subtraction 
def subtraction():
    x1=float(input("Type the first number:"))
    x2=float(input("Type the second number:"))
    print("Your difference is:")
    print( x1-x2 )

#Multiplication
def multiplication():
    x1=float(input("Type the first number:"))
    x2=float(input("Type the second number:"))
    print("Your product is:")
    print( x1*x2 )

#Division
def division():
    try:
        x1=float(input("Type the first number:"))
        x2=float(input("Type the second number:"))
        print("Your quotient is:")
        print( x1/x2 )
    except:
        print("Division by zero")

#Square Root
def sqruare_rt():
    try:
        sq=float(input("Type a positive number:"))
        print(f"The square root of number {sq} is:")
        sq= sqrt(sq)
        print( sq )
    except ValueError:
        print("You need to type a POSITIVE number")

#Logarithm with base e
def logarithm():
    try:
        lg=float(input("Type a positive number:"))
        print(f"The logarithm with base e of number {lg} is:")
        lg=log(lg)
        print( lg )
    except ValueError:
        print("You need to type a POSITIVE number")

#Power
def power():
    x1=float(input("Type the first number:"))
    x2=float(input("Type the power:"))
    print("Your result is:")
    print( x1**x2 )

#Function to determine if a number is divisible by another number
def isdiv():
    k=float(input("Type the number you want to check:"))
    n=float(input("Type the number that will do the division:"))
    if k%n==0:
        print( True )
    else:
        print( False )
    
#Sin
def sinus():
    sn=float(input("Type a number:"))
    print(f"The logarithm with base e of number {sn} is:")
    sn=sin(sn)
    print( sn )

#Cos
def cosinus():
    co=float(input("Type a number:"))
    print(f"The logarithm with base e of number {co} is:")
    co=cos(co)
    print( co )

#Help menu
def help():
    print("Type one of the following numbers and follow the given instructions to operate the program!")

#Main loop-Menu
def menu():
    while True:
        print('---Menu---')
        print('Options:\n 0)Help\n 1)Addition\n 2)Subtraction\n 3)Multiplication\n 4)Division\n 5)Square Root\n 6)Ln of number\n 7)Power\n 8)Division check\n 9)Sin\n 10)Cos\n 11)Exit')
        reply = input('Choose an option:')
        if reply == "0": help()
        elif reply == "1": addition()
        elif reply == "2": subtraction()
        elif reply == "3": multiplication()
        elif reply == "4": division()
        elif reply == "5": sqruare_rt()
        elif reply == "6": logarithm()
        elif reply == "7": power()
        elif reply == "8": isdiv()
        elif reply == "9": sinus()
        elif reply == "10": cosinus()
        elif reply == "11": break
        else:
            print("Choose an option from the menu")

menu()



    

