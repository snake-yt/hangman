# Function to set the players' names
def set_palyers():
    # Ask users to enter their names
    player_1 = str(input("\n> Nom du premier utilisateur : "))
    player_2 = str(input("\n> Nom du second joueur : (Nom ou 0) "))
    # If players didn't enter their names
    if player_1 == "":
        player_1 = "Joueur 1"
    if player_2 == "":
        player_2 = "Joueur 2"
    # If players have the same name, add 2 after player_2's name
    if player_1 == player_2:
        player_2 += " 2"
    # If the second player is a bot
    if player_2 == "0":
        player_2 = "Bot"
    # Return players name
    return player_1, player_2