from game_message import *
import random
import numpy as np


class Bot:
    def __init__(self):
        print("Initializing your super mega duper bot")
        self.last_action = None


    def get_next_move(self, game_message: TeamGameState):
        """
        Here is where the magic happens, for now the moves are not very good. I bet you can do better ;)
        """
        actions = []

        map_width = game_message.map.width
        map_height = game_message.map.height

        #print(map_width, map_height)
        tiles = game_message.map.tiles

        #My car position
        caracter_posX = game_message.yourCharacter.position.x
        caracter_posY = game_message.yourCharacter.position.y
        print(caracter_posX, caracter_posY)



        if tiles[caracter_posX][caracter_posY+1] == TileType.EMPTY:
            actions.append(MoveDownAction())
        elif tiles[caracter_posX+1][caracter_posY] == TileType.EMPTY:
            actions.append(MoveRightAction())
        elif tiles[caracter_posX][caracter_posY-1] == TileType.EMPTY:
            actions.append(MoveUpAction())
        elif tiles[caracter_posX-1][caracter_posY] == TileType.EMPTY:
            actions.append(MoveLeftAction())

        
        self.last_action = actions
        print("Actions:")
        print(actions)
        print("Tuiles")
        print(tiles)
        print(tiles[caracter_posX][caracter_posY])

        #How many bots
        nb_threat = len(game_message.threats)
        print(nb_threat)

        # Créer des listes pour stocker les coordonnées x et y des menaces
        x_positions = []
        y_positions = []

        # Parcourir chaque menace dans game_message.threats
        for threat in game_message.threats:
            # Ajouter les coordonnées x et y à leurs listes respectives
            x_positions.append(threat.position.x)
            y_positions.append(threat.position.y)




        # You can clearly do better than the random actions above! Have fun!
        return actions
