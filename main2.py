import pygame
from random import choice, randint

pygame.init()
pygame.display.init()

#  Utility functions
def loadSpriteSheet(path):
    """Load in a sprite sheet image"""
    image = pygame.image.load(path)
    return image

def spriteImage(spritesheet, size, xcoord, ycoord, width, height):
    """Function to extract an individual image from a Sprite sheet"""
    surface = pygame.Surface(size)
    surface.fill("Black")
    surface.blit(spritesheet, (0, 0), (xcoord, ycoord, width, height))
    surface.set_colorkey("Black")
    return surface

def loadImages(path, numimghor=1, numimgver=1, scaleimage=False, scalesize=(64, 64), rotateimage=False, rotation=0):
    """Function to collect all sprites from a sheet into a single list"""
    spriteSheet = loadSpriteSheet(path)
    spriteSheetWidth = spriteSheet.get_width()
    spriteSheetHeight = spriteSheet.get_height()
    spriteWidth = spriteSheetWidth // numimghor
    spriteHeight = spriteSheetHeight // numimgver

    imageList = []
    for row in range(numimgver):
        for col in range(numimghor):
            image = spriteImage(spriteSheet,
                                (spriteWidth, spriteHeight),
                                col * spriteWidth, row * spriteHeight,
                                spriteWidth, spriteHeight)
            if scaleimage == True:
                image = pygame.transform.scale(image, scalesize)
            if rotateimage == True:
                image = pygame.transform.rotate(image, rotation)
            imageList.append(image)
    return imageList

def testLoadedImages(window, xstart, ystart, imgwidth, imgheight, imglist, imgdict):
    """Test function to reflect all images on the game window."""
    for row, num in enumerate(imglist):
        for col, img in enumerate(imgdict[num]):
            window.blit(img, (xstart + (imgwidth * col), ystart + (imgheight * row)))


#  Classes
class Game:
    def __init__(self):
        self.sw = SCREENWIDTH
        self.sh = SCREENHEIGHT

        self.screen = pygame.display.set_mode((self.sw, self.sh))
        pygame.display.set_caption("Pipes")

        self.gameplay = PipeGamePlay()

        self.run = True

    def runGame(self):
        while self.run:
            self.input()
            self.update()
            self.draw()

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill("Black")
        #self.screen.blit(START["SRIGHT"][5], (500, 500))
        #testLoadedImages(self.screen, 64, 64, 64, 64, list(START.keys()), START)
        #testLoadedImages(self.screen, 64, 320, 64, 64, list(END.keys()), END)
        #testLoadedImages(self.screen, 704, 320, 64, 64, list(PIPES.keys()), PIPES)
        #testLoadedImages(self.screen, 64, 64, 64, 64, list(FLOW.keys()), FLOW)
        #testLoadedImages(self.screen, 64, 64, 64, 64, list(BOARD.keys()), BOARD)
        self.gameplay.draw(self.screen)
        pygame.display.update()

class PipeGamePlay:
    def __init__(self):
        self.rows = ROWS
        self.cols = COLUMNS

        self.grid = self._create_game_grid()
        self.pieces = {}

        self._insert_start_piece()

    def _create_game_grid(self):
        """Creates an empty game grid per the number of rows and columns"""
        grid = []
        for row in range(self.rows):
            line = []
            for col in range(self.cols):
                line.append(" ")
            grid.append(line)
        return grid

    def _insert_start_piece(self):
        """Randomly select a Starting piece, then insert it into the grid in a valid position"""
        startPiece = choice(list(START.keys()))
        validStartPos = False
        row, col = 0, 0
        while not validStartPos:
            row, col = randint(0, self.rows - 1), randint(0, self.cols - 1)
            validStartPos = self._verify_start(startPiece, self.rows, self.cols, row, col)

        self.pieces[(row, col)] = StartPiece(self, startPiece, row, col, XOFFSET, YOFFSET)
        self.grid[row][col] = self.pieces[(row, col)].piece
        return

    def _verify_start(self, startpiece, rows, cols, row, col):
        """Verify the starting location randomly selected"""
        if startpiece == "SRIGHT" and col != cols - 1: return True
        elif startpiece == "SLEFT" and col != 0: return True
        elif startpiece == "SUP" and row != 0: return True
        elif startpiece == "SDOWN" and row != rows - 1: return True
        return False

    def draw(self, window):
        for piece in self.pieces.values():
            piece.draw(window)

class StartPiece:
    def __init__(self, game, piece, row, column, xoffset, yoffset):
        self.game = game
        self.piece = piece
        self.row = row
        self.col = column
        self.xPos = xoffset + (self.col * CELLSIZE)
        self.yPos = yoffset + (self.row * CELLSIZE)
        self.imgIndex = 0

        self.image = START[self.piece][self.imgIndex]
        self.rect = self.image.get_rect(topleft=(self.xPos, self.yPos))

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.image, self.rect)


#  Constants
SCREENWIDTH = 960
SCREENHEIGHT = 896
IMAGESIZE = (64, 64)
ROWS = 12
COLUMNS = 12
CELLSIZE = 64
XOFFSET = 128
YOFFSET = 64

#  Assets
START = {
    "SRIGHT": loadImages("../Assets/pipe_start_strip11.png", 11, 1, True, IMAGESIZE),
    "SLEFT": loadImages("../Assets/pipe_start_strip11.png", 11, 1, True, IMAGESIZE, True, 180),
    "SUP":   loadImages("../Assets/pipe_start_strip11.png", 11, 1, True, IMAGESIZE, True, 90),
    "SDOWN":   loadImages("../Assets/pipe_start_strip11.png", 11, 1, True, IMAGESIZE, True, -90)
}
END = {
    "ERIGHT": loadImages("../Assets/pipe_end.png", 1, 1, True, IMAGESIZE),
    "ELEFT":   loadImages("../Assets/pipe_end.png", 1, 1, True, IMAGESIZE, True, 180),
    "EUP":   loadImages("../Assets/pipe_end.png", 1, 1, True, IMAGESIZE, True, 90),
    "EDOWN":   loadImages("../Assets/pipe_end.png", 1, 1, True, IMAGESIZE, True, -90)
}
PIPES = {
    "LR-RL": loadImages("../Assets/horizontal/pipe_horizontal.png", 1, 1, True, IMAGESIZE),
    "TB-BT": loadImages("../Assets/vertical/pipe_vertical.png", 1, 1, True, IMAGESIZE),
    "LT-TL": loadImages("../Assets/top_left/pipe_corner_top_left.png", 1, 1, True, IMAGESIZE),
    "LB-BL": loadImages("../Assets/bottom_left/pipe_corner_bottom_left.png", 1, 1, True, IMAGESIZE),
    "RT-TR": loadImages("../Assets/top_right/pipe_corner_top_right.png", 1, 1, True, IMAGESIZE),
    "RB-BR": loadImages("../Assets/bottom_right/pipe_corner_bottom_right.png", 1, 1, True, IMAGESIZE)
}
FLOW = {
    "LR": loadImages("../Assets/horizontal/water_horizontal_left_strip11.png", 11, 1, True),
    "RL": loadImages("../Assets/horizontal/water_horizontal_right_strip11.png", 11, 1, True),
    "TB": loadImages("../Assets/vertical/water_vertical_top_strip11.png", 11, 1, True),
    "BT": loadImages("../Assets/vertical/water_vertical_bottom_strip11.png", 11, 1, True),
    "LT": loadImages("../Assets/top_left/water_corner_top_left_left_strip11.png", 11, 1, True),
    "TL": loadImages("../Assets/top_left/water_corner_top_left_top_strip11.png", 11, 1, True),
    "LB": loadImages("../Assets/bottom_left/water_corner_bottom_left_left_strip11.png", 11, 1, True),
    "BL": loadImages("../Assets/bottom_left/water_corner_bottom_left_bottom_strip11.png", 11, 1, True),
    "RT": loadImages("../Assets/top_right/water_corner_top_right_right_strip11.png", 11, 1, True),
    "TR": loadImages("../Assets/top_right/water_corner_top_right_top_strip11.png", 11, 1, True),
    "RB": loadImages("../Assets/bottom_right/water_corner_bottom_right_right_strip11.png", 11, 1, True),
    "BR": loadImages("../Assets/bottom_right/water_corner_bottom_right_bottom_strip11.png", 11, 1, True)
}
BOARD = {
    "Dark": loadImages("../Assets/board/BoardDark.png", 1, 1, True),
    "Light": loadImages("../Assets/board/BoardLight.png", 1, 1, True)
}


if __name__=='__main__':
    game = Game()
    game.runGame()
    pygame.quit()