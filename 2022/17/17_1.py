import sys
import itertools

def newRow(y_max):
    yield (2, y_max)
    yield (3, y_max)
    yield (4, y_max)
    yield (5, y_max)

def newPlus(y_max):
    yield (3, y_max)
    yield (2, y_max+1)
    yield (3, y_max+1)
    yield (4, y_max+1)
    yield (3, y_max+2)

def newL(y_max):
    yield (2, y_max)
    yield (3, y_max)
    yield (4, y_max)
    yield (4, y_max+1)
    yield (4, y_max+2)

def newI(y_max):
    yield (2, y_max)
    yield (2, y_max+1)
    yield (2, y_max+2)
    yield (2, y_max+3)

def newSquare(y_max):
    yield (2, y_max)
    yield (3, y_max)
    yield (2, y_max+1)
    yield (3, y_max+1)

generators = [newRow, newPlus, newL, newI, newSquare]
sizes = [1, 3, 3, 4, 2]
shapes = itertools.cycle(zip(generators, sizes))

def pushRight(rock):
    new_rock = list()
    for (x, y) in rock:
        if x+1 < 7 and (x+1, y) not in ROCKS:
            new_rock.append((x+1, y))
        else:
            return False, rock
    
    return True, new_rock

def pushLeft(rock):
    new_rock = list()
    for (x, y) in rock:
        if x > 0 and (x-1, y) not in ROCKS:
            new_rock.append((x-1, y))
        else:
            return False, rock
    return True, new_rock

def moveDown(rock):
    new_rock = list()
    for (x, y) in rock:
        if y > 0 and (x, y-1) not in ROCKS:
            new_rock.append((x, y-1))
        else:
            return False, rock
    return True, new_rock

ROCKS = set()
top = 0
rock_count = 0
rock = None
for move in itertools.cycle(input()):
    if not rock:
        gen, rock_size = next(shapes)
        rock = frozenset(gen(top+3))
        rock_y = top+3

    if move == ">":
        moved, rock = pushRight(rock)
    elif move == "<":
        moved, rock = pushLeft(rock)

    moved, rock = moveDown(rock)
    if not moved:
        ROCKS.update(rock)
        rock = None
        top = max(top, rock_y + rock_size)
        rock_count += 1
        if rock_count == 2022:
            print(top)
            exit(0)
    else:
        rock_y -= 1
