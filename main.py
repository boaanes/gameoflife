import pygame
import globals
from board import Board, Cell

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)

color_list = (WHITE, BLACK)

size = (globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()

sprites = pygame.sprite.Group()

def game(width, height):
    loop = True

    field = Board(width,height)

    setup = list()

    for i in range(45):
        setup.append([])

    for row in setup:
        for i in range(80):
            c = Cell()
            c.set_state(0)
            row.append(c)

    setup[1][25].set_state(1)
    setup[2][23].set_state(1)
    setup[2][25].set_state(1)
    setup[3][13].set_state(1)
    setup[3][14].set_state(1)
    setup[3][21].set_state(1)
    setup[3][22].set_state(1)
    setup[3][35].set_state(1)
    setup[3][36].set_state(1)
    setup[4][12].set_state(1)
    setup[4][16].set_state(1)
    setup[4][21].set_state(1)
    setup[4][22].set_state(1)
    setup[4][35].set_state(1)
    setup[4][36].set_state(1)
    setup[5][1].set_state(1)
    setup[5][2].set_state(1)
    setup[5][11].set_state(1)
    setup[5][17].set_state(1)
    setup[5][21].set_state(1)
    setup[5][22].set_state(1)
    setup[6][1].set_state(1)
    setup[6][2].set_state(1)
    setup[6][11].set_state(1)
    setup[6][15].set_state(1)
    setup[6][17].set_state(1)
    setup[6][18].set_state(1)
    setup[6][23].set_state(1)
    setup[6][25].set_state(1)
    setup[7][11].set_state(1)
    setup[7][17].set_state(1)
    setup[7][25].set_state(1)
    setup[8][12].set_state(1)
    setup[8][16].set_state(1)
    setup[9][13].set_state(1)
    setup[9][14].set_state(1)

    field.board = setup


    for y, column in enumerate(field.board):
        for x, cell in enumerate(field.board[y]):
            cell.rect.x = globals.SCREEN_WIDTH/width * x
            cell.rect.y = globals.SCREEN_WIDTH/width * y
            sprites.add(cell)


    while loop:

        sprites.empty()

        for y, column in enumerate(field.board):
            for x, cell in enumerate(field.board[y]):
                cell.rect.x = globals.SCREEN_WIDTH/width * x
                cell.rect.y = globals.SCREEN_HEIGHT/height * y
                sprites.add(cell)


        if field.get_alive() == 0:
            loop = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False

        screen.fill(BLACK)
        sprites.draw(screen)
        pygame.display.flip()

        field.step()

        clock.tick(100)

game(globals.WIDTH, globals.HEIGHT)
pygame.quit()