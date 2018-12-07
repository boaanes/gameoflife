import random
import pygame
import globals


class Cell(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.state = random.choice([0, 1])

        self.image = pygame.Surface([globals.SCREEN_WIDTH/globals.WIDTH, globals.SCREEN_WIDTH/globals.WIDTH])
        self.image.fill(globals.BLACK)
        self.image.set_colorkey(globals.BLACK)

        self.width = globals.SCREEN_WIDTH/globals.WIDTH
        self.height = globals.SCREEN_HEIGHT/globals.HEIGHT
        self.color = self.get_color()

        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()

    def __repr__(self):
        status = 'dead'
        if self.state == 1:
            status = 'alive'
        return f'Cell(({int(self.rect.x / self.width)}, {int(self.rect.y / self.height)}), {status})'

    def get_state(self):
        return self.state

    def set_state(self, value):
        self.state = value
        self.change_color(self.get_color())

    def get_color(self):
        color = globals.BLACK

        if self.state == 1:
            color = globals.WHITE

        return color

    def change_color(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [self.rect.x, self.rect.y, self.width, self.height])


class Board:

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.board = list()

        for row in range(self.height):
            current_row = list()

            for element in range(self.width):
                cell = Cell()
                current_row.append(cell)

            self.board.append(current_row)

    def __repr__(self):
        output = ""

        for row in self.board:
            output += f'{row}\n'

        return output

    def get_alive(self):
        num_alive = 0

        for y in self.board:
            for x in y:
                if x.get_state() == 1:
                    num_alive += 1

        return num_alive

    def neighbours(self, cell):
        num_alive = 0

        x = int(cell.rect.x / cell.width)
        y = int(cell.rect.y / cell.height)

        x_coords = [x - 1, x, x + 1]
        y_coords = [y - 1, y, y + 1]

        for y_coord in y_coords:
            if y_coord < 0 or y_coord > self.height - 1:
                continue

            for x_coord in x_coords:
                if x_coord < 0 or x_coord > self.width - 1:
                    continue
                if self.board[y_coord][x_coord].get_state() == 1:
                    num_alive += 1

        if cell.get_state() == 1:
            num_alive -= 1

        return num_alive

    def step(self):
        updated_board = [list() for _ in range(self.height)]
        for row in updated_board:
            for element in range(self.width):
                row.append(0)

        current_board = self.board

        for y, column in enumerate(current_board):
            for x, cell in enumerate(current_board[y]):
                num_neighbours = self.neighbours(cell)

                if cell.get_state() == 1:
                    if num_neighbours < 2:
                        updated_board[y][x] = Cell()
                        updated_board[y][x].set_state(0)
                    elif num_neighbours > 3:
                        updated_board[y][x] = Cell()
                        updated_board[y][x].set_state(0)
                    else:
                        updated_board[y][x] = Cell()
                        updated_board[y][x].set_state(1)
                else:
                    if num_neighbours == 3:
                        updated_board[y][x] = Cell()
                        updated_board[y][x].set_state(1)
                    else:
                        updated_board[y][x] = Cell()
                        updated_board[y][x].set_state(0)

        self.board = updated_board
