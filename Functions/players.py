# Import de mon module colors
from Functions import colors

# Fonction pour définir les joueurs
def set_palyers():
    # Demander aux joueurs de rentrer leurs noms
    player_1 = str(input("\n> Nom du premier joueur : "))
    player_2 = str(input("\n> Nom du second joueur : "))
    # Tant que les noms des joueurs sont trop longs, on leur demande de les changer
    while len(player_1) > 16:
        print(colors.RED,"\n> Erreur : Le nom du premier joueur est trop long !",colors.END)
        player_1 = str(input("\n> Nom du premier joueur : "))
    while len(player_2) > 16:
        print(colors.RED,"\n> Erreur : Le nom du second joueur est trop long !",colors.END)
        player_2 = str(input("\n> Nom du second joueur : "))    
    # Si les joueurs n'entre pas de nom, on leur attribue des noms par défaut
    if player_1 == "":
        player_1 = "Joueur 1"
    if player_2 == "":
        player_2 = "Joueur 2"
    # Si les joueurs ont le même nom, on ajoute un 2 au deuxième joueur
    if player_1 == player_2:
        player_2 += " 2"
    return player_1, player_2