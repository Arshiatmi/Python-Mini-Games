import pygame

pygame.init()
screen = pygame.display.set_mode((800, 700))
done = False

x = 650
y = 150
location_x = 6
location_y = 1

# The Game Map
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

# A Function To Find Gamer Location
def find_gamer_location():
    for x, i in enumerate(game_map):
        try:
            y = i.index(2)
            return x, y
        except:
            continue

# Check If Can Go To Specific Side
def can_go(side):
    x, y = find_gamer_location()
    if side.lower() == "w":
        return (True if game_map[x][y - 1] != -1 else False)
    if side.lower() == "s":
        return (True if game_map[x][y + 1] != -1 else False)
    if side.lower() == "a":
        return (True if game_map[x - 1][y] != -1 else False)
    if side.lower() == "d":
        return (True if game_map[x + 1][y] != -1 else False)

# Function To Check If Its Win
def is_win():
    for i in game_map:
        for j in i:
            if j == 0:
                return False
    return True

WON = False

while not done:
    # Check If Won Or Not
    if is_win():
        WON = True
        done = True
    
    # Make Screen White
    screen.fill((255, 255, 255))

    # Set Color Lines
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    # Draw Lines
    for i in range(1, 9):
        pygame.draw.line(screen, BLACK, (i * 100, 0), (i * 100, 700), 4)
    for i in range(1, 8):
        pygame.draw.line(screen, BLACK, (0, i * 100), (800, i * 100), 4)

    # Handle The Boxes In The Game
    for c1, i in enumerate(game_map):
        for c2, j in enumerate(i):
            if j == -1:
                pygame.draw.rect(screen, RED, (c1 * 100 + 5, c2 * 100 + 5, 90, 90))
            if j == 1:
                pygame.draw.rect(screen, GREEN, (c1 * 100 + 5, c2 * 100 + 5, 90, 90))

    # Draw The Ball
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 45)

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if can_go("w"):
                    while game_map[location_x][location_y - 1] != -1:
                        y -= 100
                        game_map[location_x][location_y] = 1
                        game_map[location_x][location_y - 1] = 2
                        location_y -= 1
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if can_go("s"):
                    while game_map[location_x][location_y + 1] != -1:
                        y += 100
                        game_map[location_x][location_y] = 1
                        game_map[location_x][location_y + 1] = 2
                        location_y += 1
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if can_go("a"):
                    while game_map[location_x - 1][location_y] != -1:
                        x -= 100
                        game_map[location_x][location_y] = 1
                        game_map[location_x - 1][location_y] = 2
                        location_x -= 1
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if can_go("d"):
                    while game_map[location_x + 1][location_y] != -1:
                        x += 100
                        game_map[location_x][location_y] = 1
                        game_map[location_x + 1][location_y] = 2
                        location_x += 1

    pygame.display.flip()

pygame.quit()

if WON:
    from tkinter import *
    from tkinter import messagebox
    Tk().wm_withdraw()
    messagebox.showinfo('','You Won The Game Man :)')