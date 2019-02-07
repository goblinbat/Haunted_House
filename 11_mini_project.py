# Haunted House Text Game

import os

def menu():
    print("The Haunted House \n" +
          "1) Play \n" +
          "2) Exit\n")

def choice0(option):
    if option == '1':
        print('Your car breaks down in the middle of some dark spooky woods... also its raining. \n'
        'In the distance you see a house. Ignoring the fact this is the setup to a bad horror movie \n'
        'would you like to approach the house?')
        print('1) Go to the house? \n'
              '2) Leave?')
        input('>')

    elif option == '2':
        exit(1)
    else:
        print("invalid input; try again.")
        menu()

#def choice1()

menu()

options = input('input your choice: \n >')

choice0(options)

#choice1()




#def choice1():
#    print("intro description")

# while True:
#     os.system('cls||clear')


