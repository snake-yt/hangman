# Import de mes différents modules
from Functions import *


# Fonction pour demander aux joueurs s'ils veulent rejouer
def play_again():
    yes_or_not = input("\n> Voulez-vous rejouer? (o/n) ").lower().strip()
    if yes_or_not == "o":
        clear()
        main()
    else:
        print("\n> Merci d'avoir joué !")
        end_game()
        exit()


# Fonction main
def main():
    rules_or_play = input("\n> Voulez-vous lire les règles du jeu ? (o/n/enter) ").lower().strip()
    if rules_or_play == "o":
        print_rules()
    elif rules_or_play == "n":
        print("\n> C'est parti, bon amusement !")
    else:
        print("\n> C'est parti, bon amusement !")

    # Définir les joueurs
    player_1, player_2 = set_palyers()
    # Générer le mot à partir de mon module
    word = generate_words()
    display = get_word_size(word)
    # Définir les essais restants et le joueur actuel
    tries = 6
    current_player = player_1
    # Définir le gagnant et l'état du jeu
    winner = None
    game_over = False
    # Clear la console
    clear()

    # Tant que le jeu n'est pas terminé
    while not game_over:
        # Afficher le mot
        print(display)
        # Vérifier la lettre
        letter = input(f"\n> {current_player}, entrez une lettre : ").lower().strip()
        # Si la lettre est un nombre
        if letter.isdigit():
            clear()
            print(colors.RED, "\n> Erreur : Vous ne pouvez pas entrer de nombre !", colors.END)
        # SI le joueur n'entre pas de lettre
        elif letter == "":
            clear()
            print(colors.RED, "\n> Erreur : Vous devez entrer une lettre !", colors.END)
        # Si la lettre est plus longue que le mot et différente du mot  
        elif len(letter) == len(word) and letter == word:
            # Vérifier si le mot est trouvé directement
            if letter == word:
                # Définir le gagnant et l'état du jeu
                winner = current_player
                game_over = True
                # Clear la console et afficher le message de victoire
                clear()
                print(f"\n> {colors.BOLD}{winner}{colors.END} a gagné 🎉, le mot était {colors.BOLD}{word}{colors.END}.")
                # Demander aux joueurs s'ils veulent rejouer
                play_again()
        else:
            # Si la lettre est plus longue que 1 et plus courte que le mot
            if len(letter) > 1 and len(letter) < len(word):
                # Clear la console, afficher le message d'erreur et décrémenter le nombre d'essais
                clear()
                tries -= 1
                print(colors.LIGHT_RED,f"\n> Le mot {colors.BOLD}{letter}{colors.END}, n'est pas correct{colors.END}, il vous reste {tries} essais.")
            else:
                # Clear la console
                clear()
                display = update_display(word, display, letter)
                # Si la lettre n'est pas dans le mot
                if letter not in word:
                    # Décrémenter le nombre d'essais
                    tries -= 1
                    print(colors.LIGHT_RED,f"\n> La lettre {letter} n'est pas dans le mot{colors.END}, il vous reste {tries} essais.")
                    # Si le nombre d'essais est égal à 0
                    if tries == 0:
                        # Clear la console et afficher le message de défaite
                        clear()
                        print(f"\n> Personne n'a gagné, le mot à deviner était {word}.")
                        # Demander aux joueurs s'ils veulent rejouer
                        play_again()
                # Si le mot est complet
                if "_" not in display:
                    # Définir le gagnant et l'état du jeu
                    winner = current_player
                    game_over = True
                    # Clear la console et afficher le message de victoire
                    clear()
                    print(f"\n> {colors.BOLD}{winner}{colors.END} a gagné 🎉, le mot était {colors.BOLD}{word}{colors.END}.")
                    # Demander aux joueurs s'ils veulent rejouer
                    play_again()
                # Définir le joueur actuel
                current_player = player_1 if current_player == player_2 else player_2
                # Si le mot est complet et si le nombre d'essais est égal à 0
                if "_" in display and tries == 0 and game_over:
                    # Clear la console et afficher le message de défaite
                    clear()
                    print(f"\n> Personne n'a gagné, le mot était {colors.BOLD}{word}{colors.END}.")
                    # Demander aux joueurs s'ils veulent rejouer
                    play_again()


if __name__ == "__main__":
    main()
