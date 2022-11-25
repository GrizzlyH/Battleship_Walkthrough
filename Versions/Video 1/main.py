#  Module Imports
import pygame


#  Module Initialization
pygame.init()


#  Game Assets and Objects


#  Game Utility Functions


#  Game Settings and Variables
SCREENWIDTH = 1260
SCREENHEIGHT = 960


#  Colors


#  Pygame Display Initialization
GAMESCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Battle Ship')


#  Game Lists/DIctionaries


#  Loading Game Variables


#  Loading Game Sounds


#  Initialize Players


#  Main Game Loop
RUNGAME = True
while RUNGAME:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNGAME = False

    pygame.display.update()

pygame.quit()