import pygame
import globals
import pattern
import os
from board import Board

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

size = (globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game of Life")
sprites = pygame.sprite.Group()
clock = pygame.time.Clock()


def render_board(board, width, height):
    for y, column in enumerate(board):
        for x, cell in enumerate(board[y]):
            cell.rect.x = globals.SCREEN_WIDTH/width * x
            cell.rect.y = globals.SCREEN_HEIGHT/height * y
            sprites.add(cell)


def game(pat, width, height):
    loop = True

    field = Board(width, height)
    setup = pattern.set_pattern(pat, width, height)
    assert setup != 0, 'Pre-defined patterns only work if width is 80, and height is 45!'

    field.board = setup

    render_board(field.board, width, height)

    while loop:

        sprites.empty()
        render_board(field.board, width, height)

        if field.get_alive() == 0:
            loop = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False

        screen.fill(globals.BLACK)
        sprites.draw(screen)
        pygame.display.flip()

        field.step()

        clock.tick(100)


game(globals.PATTERN, globals.WIDTH, globals.HEIGHT)
pygame.quit()
