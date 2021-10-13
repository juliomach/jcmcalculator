""" Clear Screen and Test Input Numbers """

from os import system, name


def clear():
    """ Clear Screen """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def readfloat(msg):
    """ Test the Input Numbers """
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print("Error! Type a valid number.")
        except KeyboardInterrupt:
            print("No number ...")
            return 0
        else:
            return num
