import os

game_map = [
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, 0, 0, 0, 0, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1],
    [-1, 2, -1, 0, 0, 0, -1],
    [-1, -1, -1, -1, -1, -1, -1],
]


def print_map():
    print((' ') + '- ' * 7)
    for i in game_map:
        print("|", end='')
        for j in i:
            if j == -1:
                print('#|', end='')
            elif j == 0:
                print(' |', end='')
            elif j == 2:
                print('+|', end='')
            else:
                print("~|", end='')
        print()
        print((' ') + '- ' * 7)


def find_gamer_location():
    for x, i in enumerate(game_map):
        try:
            y = i.index(2)
            return x, y
        except:
            continue


def can_go(side):
    x, y = find_gamer_location()
    if side.lower() == "w":
        return (True if game_map[x - 1][y] != -1 else False)
    if side.lower() == "s":
        return (True if game_map[x + 1][y] != -1 else False)
    if side.lower() == "a":
        return (True if game_map[x][y - 1] != -1 else False)
    if side.lower() == "d":
        return (True if game_map[x][y + 1] != -1 else False)
    
def move(side):
    while can_go(side):
        x,y = find_gamer_location()
        if side == 'w':
            game_map[x][y] = 1
            game_map[x - 1][y] = 2
        elif side == 's':
            game_map[x][y] = 1
            game_map[x + 1][y] = 2
        elif side == 'a':
            game_map[x][y] = 1
            game_map[x][y - 1] = 2
        elif side == 'd':
            game_map[x][y] = 1
            game_map[x][y + 1] = 2

def is_win():
    for i in game_map:
        for j in i:
            if j == 0:
                return False
    return True

commands = ["a", "s", "d"]

moves_count = 0

while True:
    print_map()
    if can_go("w"):
        print('w',end='')
    for i in commands:
        if can_go(i):
            print('/', end='')
            print(i, end='')
    cmd = input(" : ")
    if cmd.lower() in commands or cmd.lower() == "w":
        if can_go(cmd):
            move(cmd)
    else:
        print("Please Enter A Valid Side")
    moves_count += 1
    os.system("cls")
    if is_win():
        print(f"You Won The Game ! In {moves_count} Moves.")
        print_map()
        break 
