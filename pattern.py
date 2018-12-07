from board import Board, Cell

PATTERNS = {
    "gun": [
        (1, 25),
        (2, 23), (2, 25),
        (3, 13), (3, 14), (3, 21), (3, 22), (3, 35), (3, 36),
        (4, 12), (4, 16), (4, 21), (4, 22), (4, 35), (4, 36),
        (5, 1), (5, 2), (5, 11), (5, 17), (5, 21), (5, 22),
        (6, 1), (6, 2), (6, 11), (6, 15), (6, 17), (6, 18), (6, 23), (6, 25),
        (7, 11), (7, 17), (7, 25),
        (8, 12), (8, 16),
        (9, 13), (9, 14)
    ],

    "life": [
        (20, 38), (20, 39), (20, 40), (20, 41),
        (21, 39), (21, 40), (21, 41),
        (22, 39), (22, 40), (22, 41),
        (23, 39), (23, 40), (23, 41)
    ]
}


def set_pattern(pattern, width, height):
    assert (pattern in PATTERNS or pattern == 'random'), f'{pattern} is not a valid pattern!'

    if pattern == 'random':
        return Board(width, height).board

    setup = list()

    for i in range(height):
        setup.append([])

    for row in setup:
        for i in range(width):
            c = Cell()
            c.set_state(0)
            row.append(c)

    for cell in PATTERNS[pattern]:
        setup[cell[0]][cell[1]].set_state(1)

    return setup
