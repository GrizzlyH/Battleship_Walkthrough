#  Module Imports
import pygame


#  Module Initialization
pygame.init()


#  Game Assets and Objects


#  Game Utility Functions
def createGameGrid(rows, cols, cellsize, pos):
    """Creates a game grid with coordinates for each cell"""
    startX = pos[0]
    startY = pos[1]
    coordGrid = []
    for row in range(rows):
        rowX = []
        for col in range(cols):
            rowX.append((startX, startY))
            startX += cellsize
        coordGrid.append(rowX)
        startX = pos[0]
        startY += cellsize
    return coordGrid


def createGameLogic(rows, cols):
    """Updates the game grid with logic, ie - spaces and X for ships"""
    gamelogic = []
    for row in range(rows):
        rowX = []
        for col in range(cols):
            rowX.append(' ')
        gamelogic.append(rowX)
    return gamelogic


def showGridOnScreen(window, cellsize, playerGrid, computerGrid):
    """Draws the player and computer grids to the screen"""
    gamegrids = [playerGrid, computerGrid]
    for grid in gamegrids:
        for row in grid:
            for col in row:
                pygame.draw.rect(window, (255, 255, 255), (col[0], col[1], cellsize, cellsize), 1)


def printGameLogic():
    """prints to the terminal the game logic"""
    print('Player Grid'.center(50, '#'))
    for _ in pGameLogic:
        print(_)
    print('Computer Grid'.center(50, '#'))
    for _ in cGameLogic:
        print(_)




def updateGameScreen(window):
    window.fill((0, 0, 0))

    #  Draws the player and computer grids to the screen
    showGridOnScreen(window, CELLSIZE, pGameGrid, cGameGrid)

    pygame.display.update()


#  Game Settings and Variables
SCREENWIDTH = 1260
SCREENHEIGHT = 960
ROWS = 10
COLS = 10
CELLSIZE = 50


#  Colors


#  Pygame Display Initialization
GAMESCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Battle Ship')


#  Game Lists/DIctionaries


#  Loading Game Variables
pGameGrid = createGameGrid(ROWS, COLS, CELLSIZE, (50, 50))
pGameLogic = createGameLogic(ROWS, COLS)

cGameGrid = createGameGrid(ROWS, COLS, CELLSIZE, (SCREENWIDTH - (ROWS * CELLSIZE), 50))
cGameLogic = createGameLogic(ROWS, COLS)

printGameLogic()
#  Loading Game Sounds


#  Initialize Players


#  Main Game Loop
RUNGAME = True
while RUNGAME:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNGAME = False

    updateGameScreen(GAMESCREEN)

pygame.quit()