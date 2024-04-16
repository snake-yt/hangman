# Import du module random
import random


# Fonction pour générer un mot aléatoirement
def generate_words():
    words = ["javascript", "python", "programmation","laboratoire", "sciences", "pomme", "banane", "poireau", "chips", "algorithme", "chenille", "mozilla", "logitech", "steelseries", "nvidia", "corsair"]
    word = random.randint(0, len(words)-1)
    return words[word]


# Fonction pour récupérer la taille du mot
def get_word_size(word):
    display = "_"*len(word)
    return display


# Fonction pour vérifier si la lettre est dans le mot
def check_letter(word, display, letter):
    # Convertire le mot et le display en listes
    word = list(word)
    display = list(display)
    # Si la lettre est dans le mot
    if letter in word:
        # Remplacer les underscores par la lettre
        for i in range(len(word)):
            # SI la lettre est dans le mot
            if word[i] == letter:
                # La remplacer au bon endroit
                display[i] = letter  

    return "".join(display)


# Fonction pour mettre à jour le display
def update_display(word, display, letter):
    # Modifier le display
    display = check_letter(word, display, letter)
    return display