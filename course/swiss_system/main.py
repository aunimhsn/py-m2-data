import json

# Lire le fichier players.json
with open('./data/players.json', 'r') as f:
    players = json.load(f)


# Trier les joueurs selon leur points d'elo
players_sorted = sorted(players, key=lambda player: player['elo_points'])

players_g1 = players_sorted[0:len(players_sorted)//2]
players_g2 = players_sorted[3:len(players_sorted)]

versus = []

for i in range(len(players_sorted)//2):
    versus.append([players_g1[i], players_g2[i]])

with open('./data/versus.json', 'w') as file:
    json.dump(versus, file, indent=4)

