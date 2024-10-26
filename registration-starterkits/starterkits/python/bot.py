from game_message import *
import random
import numpy as np


class Bot:
    def __init__(self):
        print("Initializing your super mega duper bot")
        self.last_action = None
        self.posX = 0
        self.posY = 0



    def get_next_move(self, game_message: TeamGameState):
        """
        Here is where the magic happens, for now the moves are not very good. I bet you can do better ;)
        """
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

        # if caracter_posX == self.posX and caracter_posY == self.posY:
        #     self.next_direction(game_message)
        self.next_direction(game_message)


        #self.last_action = actions
        print("Tuiles")
        print(tiles)
        print(tiles[caracter_posX][caracter_posY])

        actions = []

        if self.last_action == "up":
            actions.append(MoveUpAction())
        elif self.last_action == "down":
            actions.append(MoveDownAction())
        elif self.last_action == "left":
            actions.append(MoveLeftAction())
        elif self.last_action == "right":
            actions.append(MoveRightAction())

        # You can clearly do better than the random actions above! Have fun!
        return actions


    def next_direction(self, game_message: TeamGameState):

        tiles = game_message.map.tiles
        x = game_message.yourCharacter.position.x
        y = game_message.yourCharacter.position.y

        occupied_positions = set()
        for threat in game_message.threats:
            occupied_positions.add((threat.position.x, threat.position.y))
            if threat.direction == "up":
                occupied_positions.add((threat.position.x, threat.position.y - 1))
            elif threat.direction == "down":
                occupied_positions.add((threat.position.x, threat.position.y + 1))
            elif threat.direction == "left":
                occupied_positions.add((threat.position.x - 1, threat.position.y))
            elif threat.direction == "right":
                occupied_positions.add((threat.position.x + 1, threat.position.y))
            print(threat.direction)

        i_up = 1
        i_down = 1
        i_left = 1
        i_right = 1

        while tiles[x][y-i_up] == TileType.EMPTY and (x, y - i_up) not in occupied_positions:
            i_up +=1

        while tiles[x][y+i_down] == TileType.EMPTY and (x, y +i_down) not in occupied_positions:
            i_down +=1

        while tiles[x-i_left][y] == TileType.EMPTY and (x - i_left, y) not in occupied_positions:
            i_left +=1

        while tiles[x+i_right][y] == TileType.EMPTY and (x + i_right, y) not in occupied_positions:
            i_right +=1

            # Dictionnaire pour associer les actions aux directions
        direction_actions = {
            "up": (i_up-1),
            "down": (i_down-1),
            "left": (i_left-1),
            "right": (i_right-1)
        }

        # Trouver la direction avec le plus grand nombre de tuiles vides
        best_direction = max(direction_actions, key=lambda d: direction_actions[d])

        nextposX =0
        nextposY =0
        next_direction = best_direction
        # Déterminer la nouvelle position à atteindre
        if best_direction == "up":
            nextposX = x
            nextposY = y - direction_actions[best_direction]  # Position y vers le haut
        elif best_direction == "down":
            nextposX = x
            nextposY = y + direction_actions[best_direction]  # Position y vers le bas
        elif best_direction == "left":
            nextposX = x - direction_actions[best_direction]  # Position x vers la gauche
            nextposY = y
        elif best_direction == "right":
            nextposX = x + direction_actions[best_direction]  # Position x vers la droite
            nextposY = y

        print("Action en cours")
        print(self.last_action)
        print("Prochaine action")
        print(next_direction)

        if self.last_action is not None:
            print("Condition None")
            if y != self.posY or x != self.posX:
                print("condition position")
                if self.last_action == "up" and (next_direction != "down" or self.posY != y - i_up-1):
                    self.posX = nextposX
                    self.posY = nextposY
                    self.last_action = next_direction

                if self.last_action == "down" and (next_direction != "up" or self.posY != y + i_down-1):
                    self.posX = nextposX
                    self.posY = nextposY
                    self.last_action = next_direction

                if self.last_action == "left" and (next_direction != "right" or self.posX != x - i_left-1):
                    self.posX = nextposX
                    self.posY = nextposY
                    self.last_action = next_direction

                if self.last_action == "right" and (next_direction != "left" or self.posX != x + i_right-1):
                    self.posX = nextposX
                    self.posY = nextposY
                    self.last_action = next_direction
            else:
                self.posX = nextposX
                self.posY = nextposY
                self.last_action = next_direction
        else:
            self.posX = nextposX
            self.posY = nextposY
            self.last_action = next_direction


        test = "up"
        print("Action choisis")
        print(self.last_action)
        if self.last_action == "up":
            print("La condition devrait marcher")
