import os
import sys
import random
# import pygame
from threading import Thread, Lock

labirinto = [
        "PPPPPPPPPPPPPPPPPPPP",
        "P                  P",
        "P         PPPPPP   P",
        "P   PPPP       P   P",
        "P   P        PPPP  P",
        "P PPP  PPPP        P",
        "P   P     P P      P",
        "P   P     P   PPP PP",
        "P   PPP PPP   P P  P",
        "P     P   P   P P  P",
        "PPP   P   PPPPP P  P",
        "P P      PP        P",
        "P P   PPPP   PPP   P",
        "P     P    S   P   P",
        "PPPPPPPPPPPPPPPPPPPP",
    ]

class Jogador(object):
    x = 1
    y = 1

    def __init__(self):
        if labirinto[self.x][self.y] == ' ':
            labirinto[self.x][self.y] = 'O'
        else:
            for linha in labirinto:
                for coluna in linha:
                    if coluna == ' ':
                        coluna = 'O'
                        break


    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        # for wall in walls:
        #     if self.rect.colliderect(wall.rect):
        #         if dx > 0: # Moving right; Hit the left side of the wall
        #             self.rect.right = wall.rect.left
        #         if dx < 0: # Moving left; Hit the right side of the wall
        #             self.rect.left = wall.rect.right
        #         if dy > 0: # Moving down; Hit the top side of the wall
        #             self.rect.bottom = wall.rect.top
        #         if dy < 0: # Moving up; Hit the bottom side of the wall
        #             self.rect.top = wall.rect.bottom

def desenharLabirinto(labirinto):
    for linha in labirinto:
        print(linha)

def main():
    # P = Parede
    # S = Saída

    desenharLabirinto(labirinto)
    # while(1):
    Jogador()
    print("Jogador Adicionado")
    desenharLabirinto(labirinto)

    print("Main")

if __name__ == "__main__":
    main()