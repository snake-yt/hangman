# Import colorama module
from colorama import init, Fore
init()

# Function to set the players' names
def set_palyers():
    # Ask players to enter their names
    player_1 = str(input("\n> Nom du premier joueur : "))
    player_2 = str(input("\n> Nom du second joueur : "))
    # If players's name is to long 
    while len(player_1) > 16:
        print(Fore.RED,"\n> Erreur : Le nom du premier joueur est trop long !",Fore.WHITE)
        player_1 = str(input("\n> Nom du premier joueur : "))
    while len(player_2) > 16:
        print(Fore.RED,"\n> Erreur : Le nom du second joueur est trop long !",Fore.WHITE)
        player_2 = str(input("\n> Nom du second joueur : "))    
    # If players didn't enter their names
    if player_1 == "":
        player_1 = "Joueur 1"
    if player_2 == "":
        player_2 = "Joueur 2"
    # If players have the same name, add 2 after player_2's name
    if player_1 == player_2:
        player_2 += " 2"
    # Return players name
    return player_1, player_2