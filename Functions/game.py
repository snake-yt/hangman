# Import os and colors
from Functions import colors
import os


# Print rules function
def print_rules():
    print(f"\n----------------Bienvenue dans notre jeu du pendu en {colors.YELLOW}Python{colors.END} !----------------")
    print("\n---------------------------Noah, Matthew et Yollan---------------------------")
    print("\nVoici les règles du jeu :")
    print("\n> 1. Créez vos noms d'utilisateurs (maximum 16 caractères).")
    print("> 2. Si vous avez tout deux le même nom d'utilisateur, celui du deuxième joueur sera suivi d'un 2.")
    print(f"> 3. Si vous faites une entrée au lieu d'entrer un nom d'utilisateur, vos noms par défaut seront {colors.BOLD}Joueur 1{colors.END} et {colors.BOLD}Joueur 2{colors.END}.")
    print("> 4. Un mot est choisi dans une liste prédéfinie, et vous devez en deviner ses lettres chacun à votre tour.")
    print("> 5. Vous avez le droit à 6 essais pour trouver le mot, vous ne perdez pas d'essais, si vous faites une erreur.")
    print("> 6. Si vous trouvez directement le mot, vous pouvez l'écrire entièrement.")
    print("> 7. Vous ne pouvez écrire que des caractères alphabétiques (pas de chiffres, de symboles, etc.")
    print("> 8. Le premier joueur à compléter ou à trouver le mot gagne la partie.")
    print("> 9. Pour plus de questions, n'hésitez pas à nous appeler.")
    print("\n----------------------https://github.com/snake-yt/hangman--------------------")
    print("\n------------------------Bonne chance et amusez-vous !------------------------")

# Clear function
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# End game function
def end_game():
    os.system("pause")
    os.system("cls" if os.name == "nt" else "clear")    