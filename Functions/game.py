# Import os and main 
import os
from main import main


# Print rules function
def print_rules():
    print("\n----------------Bienvenue dans notre jeu du pendu en Python !----------------")
    print("\n---------------------------Noah, Matthew et Yollan---------------------------")
    print("\nLes règles sont simples :")
    print("\n> 1. Créer votre nom d'utilisateur, si le nom du deuxième joueur est le même que le premier, il sera suivit d'un 2 et il ne peut dépasser 16 caractères.")
    print("> 2. Un mot est choisi dans une liste prédéfinie, et vous devez en deviner ses lettres chacun à votre tour.")
    print("> 3. Vous avez le droit à 6 essais pour trouver le mot.")
    print("> 4. Si vous entrez plus d'une lettre, un mot ou un nombre, vous aurez une erreur et vous perdrez un essai.")
    print("> 5. Le premier joueur à compléter le mot gagne la partie.")
    print("\n----------------------https://github.com/snake-yt/hangman--------------------")
    print("\n------------------------Bonne chance et amusez-vous !------------------------")


# End game function
def end_game():
    os.system("pause")
    os.system("cls" if os.name == "nt" else "clear")