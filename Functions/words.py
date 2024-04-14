# Import the random module
import random


# Function to generate a random word from a list of words
def generate_words():
    # List of words
    words = ["javascript", "python", "programmation",
             "laboratoire", "sciences", "pomme", "banane"]
    # Return a random word
    return random.choice(words)


# Function to get the size of the word
def get_word_size(word):
    # Create a display for the word with "_"
    display = "_"*len(word)
    # Return the display
    return display


# Function to check if the letter is in the word
def check_letter(word, display, letter):
    # Convert the word and the display to a list
    word = list(word)
    display = list(display)
    # If the letter is in the word
    if letter in word:
        # Replace "_" with the letter
        for i in range(len(word)):
            # If the letter is in the word
            if word[i] == letter:
                display[i] = letter

    # Return the display
    return "".join(display)


# Function to update the display
def update_display(word, display, letter):
    # Update and return the display
    display = check_letter(word, display, letter)
    return display


