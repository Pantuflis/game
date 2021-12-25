import os
import time
from art import game_over_art, dungeon_art, city_art, elfs_art, end_art

stories = {
    'first_level': "Eres una hermosa y fuerte elfa oscura, te encuentras en una catacumba desolada\ny de repente escuchas ruidos extraños...",
    'second_level': "Te diriges hacia los ruidos y ves a un delgado elfo en el suelo,\nesta rodeado de terribles monstruos...",
    'third_level': "Con tu gran poder has logrado derrotar a todos los monstruos y quedas sola con el...",
    'fourth_level': "Ayudas al debilitado elfo y cuando puede abrir sus ojos queda impresionado con tu belleza...",
    'fifth_level': "Te sonrojas ante la mirada del aun debil pero tierno elfo y no puedes evitar sonreir.\nAl ver tu sonrisa queda perdidamente enamorado y te invita a volver a la ciudad...",
    'sixth_level': "Vuelven a la ciudad y el elfo te dice su nombre, Devilwarrior y tu el tuyo, Cameron.\nDevilwarrior luce su armadura frente a ti para impresionarte...",
    'seventh_level': "Devilwarrior se alegra con tus halagos y comienza a contarte sus historias,\nsus batallas, sus victorias y derrotas...",
    'eighth_level': "Al escuchar tus historias Devilwarrior se da cuenta de lo buena que eres y cuanto te quiere.\nAl notar esto toma una gran desicion, te invita a emprender una nueva aventura junto a el...",
    'ninth_level': "Aceptas la propuesta de Devilwarrior y comienzan una nueva aventura juntos.\nSera la mas larga aventura que hayan empredido, pero tambien sera la mejor.",
}

def story_and_art(story, art):
    os.system('cls')
    print(art)
    print(story)

def game_over():
    os.system('cls')
    print(game_over_art)
    print("\n==========================================\n")
    print("Este no es tu destino, vuelve a intentarlo")
    print("\n==========================================\n")
    time.sleep(3)
    first_level()

def invalid_option(level):
    print("\nElija una opcion valida\n")
    time.sleep(2)
    level

def first_level():
    story_and_art(stories['first_level'], dungeon_art)
    option = input("\nOpciones:\n[1] Salir de la catacumba\n[2] Ir hacia los ruidos\nQue haces?: ")
    if option == "1":
        game_over()
    elif option == "2":
        second_level()
    else:
        invalid_option(first_level)


def second_level():
    story_and_art(stories['second_level'], dungeon_art)
    option = input("\nOpciones:\n[1] Combatir los montruos para ayudar al elfo\n[2] Escapar y dejar morir al elfo\nQue haces?: ")
    if option == "1":
        third_level()
    elif option == "2":
        game_over()
    else:
        invalid_option(second_level)

def third_level():
    story_and_art(stories['third_level'], dungeon_art)
    option = input("\nOpciones:\n[1] Robar todas sus pertenencias y escapar\n[2] Ayudarlo a levantarse y recuperarse del ataque\nQue haces?: ")
    if option == "1":
        game_over()
    elif option == "2":
        fourth_level()
    else:
        invalid_option(third_level)

def fourth_level():
    story_and_art(stories['fourth_level'], dungeon_art)
    option = input("\nOpciones:\n[1] Sonrojarse\n[2] Soltarlo y escapar\nQue haces?: ")
    if option == "1":
        fifth_level()
    elif option == "2":
        game_over()       
    else:
        invalid_option(fourth_level)

def fifth_level():
    story_and_art(stories['fifth_level'], dungeon_art)
    option = input("\nOpciones:\n[1] Abandonar al elfo y seguir investigando la catacumba\n[2] Volver a la ciudad con el elfo\nQue haces?: ")
    if option == "1":
        game_over()       
    elif option == "2":
        sixth_level()
    else:
        invalid_option(fifth_level)

def sixth_level():
    story_and_art(stories['sixth_level'], city_art)
    option = input("\nOpciones:\n[1] Reirte y burlarte\n[2] Halagar su armadura\nQue haces?: ")
    if option == "1":
        game_over()     
    elif option == "2":
        seventh_level()
    else:
        invalid_option(sixth_level)

def seventh_level():
    story_and_art(stories['seventh_level'], elfs_art)
    option = input("\nOpciones:\n[1] Contar tus historias\n[2] Negarte a contar tus historias\nQue haces?: ")
    if option == "1":
        eighth_level()
    elif option == "2":
        game_over()
    else:
        invalid_option(seventh_level)

def eighth_level():
    story_and_art(stories['eighth_level'], elfs_art)
    option = input("\nOpciones:\n[1] Aceptar ir a la nueva aventura\n[2] Rechazar la nueva aventura y seguir tu camino\nQue haces?: ")
    if option == "1":
        ninth_level()
    elif option == "2":
        game_over()
    else:
        invalid_option(eighth_level)

def ninth_level():
    story_and_art(stories['ninth_level'], end_art)
    print("\n========================\n")
    print("Haz alcanado tu destino")
    print("\n========================\n")
    time.sleep(3)
    input("Presiona Enter para salir")