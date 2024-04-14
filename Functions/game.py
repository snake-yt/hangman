# Import os and main 
import os


# Print rules function
def print_rules():
    print("\n----------------Bienvenue dans notre jeu du pendu en Python !----------------")
    print("\n---------------------------Noah, Matthew et Yollan---------------------------")
    print("\nVoici les règles du jeu :")
    print("\n> 1. Créer votre nom d'utilisateur (max 16) et si le nom du deuxième joueur est le même que le premier, il sera suivit d'un 2.")
    print("> 2. Un mot est choisi dans une liste prédéfinie, et vous devez en deviner ses lettres chacun à votre tour.")
    print("> 3. Vous avez le droit à 6 essais pour trouver le mot. Vous ne perdez pas d'essai si vous êtes comfronté à une erreur.")
    print("> 4. Si vous trouvez directement le mot, vous pouvez l'écrire entièrement.")
    print("> 5. Vous ne pouvez écrire qu'une seule lettre à la fois et seulement des lettres.")
    print("> 6. Le premier joueur à compléter le mot gagne la partie.")
    print("\n----------------------https://github.com/snake-yt/hangman--------------------")
    print("\n------------------------Bonne chance et amusez-vous !------------------------")


# End game function
def end_game():
    os.system("pause")
    os.system("cls" if os.name == "nt" else "clear")