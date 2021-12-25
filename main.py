from art import title
from game import first_level
import time
import os


def menu():
    os.system('cls')

    # Title
    print(title)

    # Description
    print("\n==========================================\n")
    print("Adentrate en una hitoria que no olvidaras")
    print("\n==========================================\n")

    # Menu
    print("[1] Comenzar la aventura")
    print("[2] Salir")
    menu_option = input("Elige una opcion: ")
    return menu_option

def select_option():
    start_game = False
    while not start_game:
        option = menu()
        if option == "1":
            start_game = True
            first_level()
        elif option == "2":
            start_game = True
        else:
            print("\nElija una opcion valida\n")
            time.sleep(2)

if __name__ == "__main__":
    select_option()