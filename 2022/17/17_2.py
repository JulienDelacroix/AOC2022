import sys
import itertools
from queue import Queue

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

def cleanRocks(top, rocks):
    visited = set()
    new_rocks = set()
    q = Queue()
    q.put((0, top+1))
    visited.add((0, top+1))

    def arroundNoUp(pos):
        x, y = pos
        yield (x, y - 1)
        if x+1 < 7: yield (x + 1, y)
        if x > 0: yield (x - 1, y)

    min_y = 100000
    while not q.empty():
        pos = q.get()
        for next_pos in arroundNoUp(pos):
            if next_pos in rocks:
                new_rocks.add(next_pos)
                min_y = min(min_y, next_pos[1])
            elif next_pos not in visited:
                q.put(next_pos)
                visited.add(next_pos)

    return set((x, y - min_y) for (x,y) in new_rocks), min_y

ROCKS = set()
for x in range(0,7):
    ROCKS.add((x, -1))

tracker = {}
cycle = None

result = 0
top = -1
rock = None
rock_count = 0
move_count = 0

pattern = input()
for move in itertools.cycle(pattern):
    move_count += 1
    if not rock:
        gen, rock_size = next(shapes)
        rock = frozenset(gen(top+4))

    if move == ">":
        moved, rock = pushRight(rock)
    elif move == "<":
        moved, rock = pushLeft(rock)

    moved, _ = moveDown(rock)
    if moved:
        moved, rock = moveDown(rock)

    if not moved:
        ROCKS.update(rock)
        rock = None

        new_top = max(y for (_,y) in ROCKS)
        result += (new_top - top)
        top = new_top
        ROCKS, offset = cleanRocks(top, ROCKS)
        top -= offset

        rock_count += 1
        MAX = 1000000000000
        if rock_count == MAX:
            print(result)
            exit(0)

        if not cycle:
            key = frozenset(ROCKS), (move_count % len(pattern)), (rock_count % 5)
            if key in tracker:
                prev_rock, prev_result = tracker[key]
                cycle_length = (rock_count - prev_rock)
                cycle_value  = result - prev_result
                cycle = (rock_count, cycle_length, cycle_value)
                print("Found cycle", cycle, "at step", rock_count)
            tracker[key] = rock_count, result
        else:
            cycle_start, cycle_length, cycle_value = cycle
            if rock_count == cycle_start + cycle_length:
                loops, remaining = divmod(MAX - rock_count, cycle_length)
                rock_count = MAX - remaining
                result += loops * cycle_value
                print("Looping", loops, "times with cycle_value", cycle_value, "remaining step =", remaining)
