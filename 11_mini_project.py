# Haunted House Text Game

import os

def menu():
    print("The Haunted House \n" +
          "1) Play \n" +
          "2) Exit\n")
    x = input('input your choice: \n' +
          '>')

menu()
def choice0(option):
    option = x
    if option == '1':
        print('print')
    elif option == '2':
        exit(1)
    else:
        print("invalid input; try again.")
        menu()



#def choice1():
#    print("intro description")

# while True:
#     os.system('cls||clear')


