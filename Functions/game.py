# Import os and main 
import os
from main import main


# Print rules function
def print_rules():
    print("\n----------------Bienvenue dans notre jeu du pendu en Python !----------------")
    print("\n---------------------------Noah, Matthew et Yollan---------------------------")
    print("\nLes règles sont simples :")
    print("\n> 1. Vous devez créer vos utilisateurs, ou un utisateur peut jouer contre un bot.")
    print("> 2. Un mot est choisi dans une liste prédéfinie, et vous devez le deviner chacun votre tour.")
    print("> 3. Vous avez le droit à 6 essais pour trouver le mot.")
    print("> 4. Si vous entrez plus d'une lettre, un mot ou un nombre, vous aurez une erreur.")
    print("> 5. Le premier joueur à trouver le mot a gagné.")
    print("> 6. Vous pouvez accéder au règles du jeu en faisant \"rules\"")


# End game function
def end_game():
    os.system("pause")
    os.system("cls" if os.name == "nt" else "clear")