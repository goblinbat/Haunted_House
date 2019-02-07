# Haunted House Text Game

import os
x = True

def menu():
    print("The Haunted House \n" +
          "1) Play \n" +
          "2) Exit\n")

def choice0(option):
    if option == '1':
        print('Your car breaks down in the middle of some dark spooky woods... also its raining. \n' +
        'In the distance you see a house. \n' +
        'would you like to approach the house?')
        print('1) Go to the house? \n'
              '2) Leave?')

    elif option == '2':
        exit(1)
    else:
        print("invalid input; try again.")
        choice0


def choice1(option):
    if option == '1':
        print('Ignoring the fact this is the setup to a bad horror movie, you approach the house. \n')
        print('You are soaked to the bone by the time you reach the front door.\n' +
              "Trying to open it and get out of the rain, you find it's locked.\n" +
              'Fortunately, you spot a cellar door off to the side. Try and open it? \n')
        print('1) try and open the cellar door \n' +
              '2) knock on the front door \n' +
              '3) try and break down the front door \n')
    if option == '2':
        print("too bad, there's nowhere else to go.")
        print('You are soaked to the bone by the time you reach the front door.\n' +
              "Trying to open it and get out of the rain, you find it's locked.\n" +
              'Fortunately, you spot a cellar door off to the side. Try and open it? \n')
        print('1) try and open the cellar door \n' +
              '2) knock on the front door \n'+
              '3) try and break down the front door \n')
    else:
        print('invalid input; try again.')
        choice1(option)




menu()

option0 = input('input your choice: \n >')
option1 = input('input your choice: \n >')
option2 = input('input your choice: \n >')

while x == True:
    choice0(option0)
    option1
    x = False


Choice1(option1)
option2







#def choice1():
#    print("intro description")

# while True:
#     os.system('cls||clear')


