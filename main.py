# Import all functions of my module
from Functions import *

# Play again function
def play_again():
    yes_or_not = input("\n> Voulez-vous rejouer? (o/n) ").lower().strip()
    if yes_or_not == "o":
        main()
    else:
        print("\n> Merci d'avoir joué !")
        end_game()
        exit()


# main function
def main():
    rules_or_play = input("\n> Voulez-vous lire les règles du jeu ? (o/n/enter) ").lower().strip()
    if rules_or_play == "o":
        print_rules()
    elif rules_or_play == "n":
        print("\n> C'est parti, bon amusement !")
    else:
        print("\n> C'est parti, bon amusement !")

    # Set the players
    player_1, player_2 = set_palyers()
    # Generate a random word and get his size
    word = generate_words()
    display = get_word_size(word)
    # Set the number of tries and the current player
    tries = 6
    current_player = player_1
    # Set the winner and game status
    winner = None
    game_over = False
    # Clear console
    clear()

    # While the game is not over
    while not game_over:
        # Display the word
        print(display)
        # Check letters
        letter = input(f"\n> {current_player}, entrez une lettre : ").lower().strip()
        if letter.isdigit():
            clear()
            print(colors.RED, "\n> Erreur : Vous ne pouvez pas entrer de nombre !", colors.END)
        # If the letter is empty
        elif letter == "":
            clear()
            print(colors.RED, "\n> Erreur : Vous devez entrer une lettre !", colors.END)
        # If the letter is the same as the word    
        elif len(letter) == len(word) and letter == word:
            # Check if the word is completed instantly
            if letter == word:
                # Set the winner and game status
                winner = current_player
                game_over = True
                # Clear console & and display the win message
                clear()
                print(f"\n> {colors.BOLD}{winner}{colors.END} a gagné 🎉, le mot était {colors.BOLD}{word}{colors.END}.")
                # Ask players if they want to play again
                play_again()
        else:
            # If the letter is more than one and inferior to the word
            if len(letter) > 1 and len(letter) < len(word):
                # Clear console & and display error
                clear()
                print(colors.RED, "\n> Erreur : Vous ne pouvez entrer qu'une seule lettre !", colors.END)
            else:
                # Clear console & and update the display
                clear()
                display = update_display(word, display, letter)
                # If the letter is not in the word
                if letter not in word:
                    # Decrease the number of tries and display the number of tries left
                    tries -= 1
                    print(colors.LIGHT_RED,f"\n> La lettre {letter} n'est pas dans le mot.",colors.END,f"Il vous reste {tries} essais.")
                    # If the number of tries is 0 & if the word is not complete
                    if tries == 0:
                        # Clear console & and display the lose message
                        clear()
                        print(f"\n> Personne n'a gagné, le mot à deviner était {word}.")
                        # Ask players if they want to play again
                        play_again()
                # If the word is complete
                if "_" not in display:
                    # Set the winner and game status
                    winner = current_player
                    game_over = True
                    # Clear console & and display the win message
                    clear()
                    print(f"\n> {colors.BOLD}{winner}{colors.END} a gagné 🎉, le mot était {colors.BOLD}{word}{colors.END}.")
                    # Ask players if they want to play again
                    play_again()
                # Change the current player
                current_player = player_1 if current_player == player_2 else player_2
                # If the world is not completed and the number of tries is 0 and the game is over
                if "_" in display and tries == 0 and game_over:
                    # Clear console & and display the lose message
                    clear()
                    print(f"\n> Personne n'a gagné, le mot était {colors.BOLD}{word}{colors.END}.")
                    # Ask players if they want to play again
                    play_again()


if __name__ == "__main__":
    main()
