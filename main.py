import pygame
import globals
import pattern
from board import Board

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

color_list = (WHITE, BLACK)

size = (globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()

sprites = pygame.sprite.Group()


def game(pat, width, height):
    loop = True

    field = Board(width, height)
    setup = pattern.set_pattern(pat, width, height)

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


game(globals.PATTERN, globals.WIDTH, globals.HEIGHT)
pygame.quit()
