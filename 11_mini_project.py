# Haunted House Text Game

import os

def menu():
    print("The Haunted House \n" +
          "1) Play \n" +
          "2) Exit\n")

def choice0(option):
    if option == '1':
        print('Your car breaks down in the middle of some dark spooky woods... also its raining. \n'
        'In the distance you see a house. \n'
        'would you like to approach the house?')
        print('1) Go to the house? \n'
              '2) Leave?')

    elif option == '2':
        exit(1)
    else:
        print("invalid input; try again.")
        choice0(options)

def choice1(option):
    if option == '1':
        print('Ignoring the fact this is the setup to a bad horror movie, you approach the house. \n')
        print('You are soaked to the bone by the time you reach the front door.\n'
              "Trying to open it and get out of the rain, you find it's locked.\n"
              'Fortunately, you spot a cellar door off to the side. Try and open it? \n')
        print('1) try and open the cellar door \n'
              '2) knock on the front door \n'
              '3) try and break down the front door \n')
    if option == '2':
        print("too bad, there's nowhere else to go.")
        print('You are soaked to the bone by the time you reach the front door.\n'
              "Trying to open it and get out of the rain, you find it's locked.\n"
              'Fortunately, you spot a cellar door off to the side. Try and open it? \n')
        print('1) try and open the cellar door \n'
              '2) knock on the front door \n'
              '3) try and break down the front door \n')
    else:
        print('invalid input; try again.')
        choice1(options)


menu()

options = input('input your choice: \n >')

choice0(options)
options = input('input your choice: \n >')

choice1(options)
options = input('input your choice: \n >')




#def choice1():
#    print("intro description")

# while True:
#     os.system('cls||clear')


