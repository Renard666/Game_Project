
from pprint import pprint
from random import *
is_game_started = True

game_map = [

    ["#","#","#","#","#","#","#","#","#"],
    ["#","0","0","0","0","0","0","0","#"],
    ["#","0","0","0","0","0","0","0","#"],
    ["#","0","0","0","0","0","0","0","#"],
    ["#","0","0","0","0","0","0","0","#"],
    ["#","0","0","0","0","0","0","0","#"],
    ["#","0","#","0","0","0","#","0","#"],
    ["#","0","0","0","0","0","0","0","#"],
    ["#","#","#","#","#","#","#","#","#"]
]

# "🐄""🐄"

def get_random_tile():
    # select a random line in the map
    y = randrange(len(game_map)-1)
    # select a random column/tile in the line
    x = randrange (len(game_map[y])-1)

    tile = game_map[y][x]

    # if it's a wall, restart
    if (tile == "#"):
        return get_random_tile()

    return (x, y, game_map[y][x])

    
#game_map[y[x]] = "🐄"
#pprint(game_map)


# objectif: case de depart pour le joueur
# initial_player_position = 
# print(initial_player_position)



#    low = 0 
#    high len(list)-1
    
#    while low <= high:
    #    player_position = 
    #    return


#(x,y) = player_position


#print: game_map[x][y]

# avant de démarrer le jeu
# ajouter le joueur sur la carte

#while is_game_started:
        
#    pprint(game_map)

    # parcourir chaque ligne
#    for (y, line) in enumerate(game_map):
        # si le joueur est dans la ligne
        # stocker sa position x et y
        # sinon, gérer l'erreur

#        player_input = input()

#            if player_input == "d":
#               game_map[1][1] = "0"
#                game_map[1][2] = "9"
                

#            elif player_input == "q":
#                game_map[1][1] = "0"
#                game_map[1][0] = "9"
#                

#            elif player_input == "z":
#                game_map[1][1] = "0"
#                game_map[0][1] = "9"
#                

#            elif player_input == "s":
#                game_map[1][1] = "0"
#                game_map[2][1] = "9"
                

#            elif player_input == "@":
#                is_game_started = False

#            else: print(game_map,"click on the right button or leave with @ ")




# define:
    # # = wall
    # 9 = player
    # 6 = enemy
    # 0 = hole
    
    #define a class for each string




