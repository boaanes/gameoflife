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
    ],

    "life2": [
        (22, 30), (22, 31), (22, 32), (22, 33), (22, 34), (22, 35), (22, 36), (22, 37),
        (22, 39), (22, 40), (22, 41), (22, 42), (22, 43),
        (22, 47), (22, 48), (22, 49),
        (22, 56), (22, 57), (22, 58), (22, 59), (22, 60), (22, 61), (22, 62),
        (22, 64), (22, 65), (22, 66), (22, 67), (22, 68)
    ],

    "life3": [
        (20, 42),
        (21, 40), (21, 42), (21, 43),
        (22, 40), (22, 42),
        (23, 40),
        (24, 38),
        (25, 36), (25, 38)
    ],

    "life4": [
        (20, 37), (20, 38), (20, 39), (20, 41),
        (21, 37),
        (22, 40), (22, 41),
        (23, 38), (23, 39), (23, 41),
        (24, 37), (24, 39), (24, 41)
    ]

}


def set_pattern(pattern, width, height):
    assert (pattern in PATTERNS or pattern == 'random'), f'{pattern} is not a valid pattern!'

    if (width != 80 or height != 45) and pattern != 'random':
        return 0

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
