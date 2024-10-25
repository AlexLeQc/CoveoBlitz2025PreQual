from game_message import *
import random
import numpy as np


class Bot:
    def __init__(self):
        print("Initializing your super mega duper bot")
        self.last_action = None
        self.posX = None
        self.posY = None
        self.firstaction = False


    def get_next_move(self, game_message: TeamGameState):
        """
        Here is where the magic happens, for now the moves are not very good. I bet you can do better ;)
        """
        if not self.firstaction:
            self.next_direction(game_message)
            self.firstaction = True

        map_width = game_message.map.width
        map_height = game_message.map.height

        #print(map_width, map_height)
        tiles = game_message.map.tiles

        #My car position
        caracter_posX = game_message.yourCharacter.position.x
        caracter_posY = game_message.yourCharacter.position.y
        print(caracter_posX, caracter_posY)

        occupied_positions = set()
        for threat in game_message.threats:
            occupied_positions.add((threat.position.x, threat.position.y))


        if caracter_posX == self.posX and caracter_posY == self.posY:
            self.next_direction(game_message)


        # if tiles[caracter_posX][caracter_posY+1] == TileType.EMPTY and (caracter_posX, caracter_posY + 1) not in occupied_positions:
        #     actions.append(MoveDownAction())
        # elif tiles[caracter_posX+1][caracter_posY] == TileType.EMPTY and (caracter_posX+1, caracter_posY) not in occupied_positions:
        #     actions.append(MoveRightAction())
        # elif tiles[caracter_posX][caracter_posY-1] == TileType.EMPTY and (caracter_posX, caracter_posY - 1) not in occupied_positions:
        #     actions.append(MoveUpAction())
        # elif tiles[caracter_posX-1][caracter_posY] == TileType.EMPTY and (caracter_posX-1, caracter_posY) not in occupied_positions:
        #     actions.append(MoveLeftAction())
        # else:
        #     actions.append(MoveRightAction())



        #self.last_action = actions
        print("Actions:")
        print("Tuiles")
        print(tiles)
        print(tiles[caracter_posX][caracter_posY])




        # You can clearly do better than the random actions above! Have fun!
        return self.last_action


    def next_direction(self, game_message: TeamGameState):

        tiles = game_message.map.tiles
        x = game_message.yourCharacter.position.x
        y = game_message.yourCharacter.position.y

        i_up = 1
        i_down = 1
        i_left = 1
        i_right = 1

        while tiles[x][y-i_up] == TileType.EMPTY:
            i_up +=1

        while tiles[x][y+i_down] == TileType.EMPTY:
            i_down +=1

        while tiles[x-i_left][y] == TileType.EMPTY:
            i_left +=1

        while tiles[x+i_right][y] == TileType.EMPTY:
            i_right +=1

            # Dictionnaire pour associer les actions aux directions
        direction_actions = {
            "up": (i_up-1, MoveUpAction),
            "down": (i_down-1, MoveDownAction),
            "left": (i_left-1, MoveLeftAction),
            "right": (i_right-1, MoveRightAction)
        }

        # Trouver la direction avec le plus grand nombre de tuiles vides
        best_direction = max(direction_actions, key=lambda d: direction_actions[d][0])

        # Déterminer la nouvelle position à atteindre
        if best_direction == "up":
            self.posX = x
            self.posY = y - direction_actions[best_direction][0]  # Position y vers le haut
        elif best_direction == "down":
            self.posX = x
            self.posY = y + direction_actions[best_direction][0]  # Position y vers le bas
        elif best_direction == "left":
            self.posX = x - direction_actions[best_direction][0]  # Position x vers la gauche
            self.posY = y
        elif best_direction == "right":
            self.posX = x + direction_actions[best_direction][0]  # Position x vers la droite
            self.posY = y

        self.last_action = [direction_actions[best_direction][1]()]


