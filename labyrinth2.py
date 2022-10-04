import os
import sys
import random
import pygame
from threading import Thread, Lock

screen = pygame.display.set_mode((320, 240))
walls = []
level = [
        "WWWWWWWWWWWWWWWWWWWW",
        "W                  W",
        "W         WWWWWW   W",
        "W   WWWW       W   W",
        "W   W        WWWW  W",
        "W WWW  WWWW        W",
        "W   W     W W      W",
        "W   W     W   WWW WW",
        "W   WWW WWW   W W  W",
        "W     W   W   W W  W",
        "WWW   W   WWWWW W  W",
        "W W      WW        W",
        "W W   WWWW   WWW   W",
        "W     W    E   W   W",
        "WWWWWWWWWWWWWWWWWWWW",
        ]

class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

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
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

def GameOn(id, end_rect, colorA, colorB):
    print("Hello {}".format(id))
    player = Player()

    running = True
    while running:
        
        # clock.tick(60)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

        # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and id == 1:
            player.move(-2, 0)
        elif key[pygame.K_LEFT] and id == 2:
            player.move(-2, 0)
        if key[pygame.K_d] and id == 1:
            player.move(2, 0)
        elif key[pygame.K_RIGHT and id == 2]:
            player.move(2, 0)
        if key[pygame.K_w] and id == 1:
            player.move(0, -2)
        elif key[pygame.K_UP] and id == 2:
            player.move(0, -2)
        if key[pygame.K_s] and id == 1:
            player.move(0, 2)
        elif key[pygame.K_DOWN] and id == 2:
            player.move(0, 2)

        # Just added this to make it slightly fun ;)
        if player.rect.colliderect(end_rect):
            return 0
            # pygame.quit()
            # sys.exit()
        
        screen.fill((0, 0, 0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        pygame.draw.rect(screen, (colorA, colorB, 0), player.rect)
        # gfxdraw.filled_circle(screen, 255, 200, 5, (0,128,0))
        pygame.display.flip()

def main():
    # Initialise pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()

    # Set up the display
    pygame.display.set_caption("Get to the red square!")

    x = y = 0
    for row in level:
        for col in row:
            if col == "W":
                Wall((x, y))
            if col == "E":
                end_rect = pygame.Rect(x, y, 16, 16)
            x += 16
        y += 16
        x = 0
    
    # Draw the scene
    # screen.fill((0, 0, 0))
    # for wall in walls:
    #     pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    # pygame.draw.rect(screen, (255, 0, 0), end_rect)
    # # pygame.draw.rect(screen, (255, 200, 0), player.rect)
    # # gfxdraw.filled_circle(screen, 255, 200, 5, (0,128,0))
    # pygame.display.flip()

    playerOne = Thread(target = GameOn(1, end_rect, random.randint(100, 255), random.randint(100, 255)))
    playerTwo = Thread(target = GameOn(2, end_rect, random.randint(100, 255), random.randint(100, 255)))

    playerOne.start()
    print("Debug\n")
    playerTwo.start()

    # threads.append(playerOne)
    # threads.append(playerTwo)

    playerOne.join()
    playerTwo.join()

if __name__ == "__main__":
    main()
