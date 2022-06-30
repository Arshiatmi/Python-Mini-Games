from classes import *
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 700))
done = False
WON = False

a = Game()


def button(screen, position, text, color=(0, 0, 0), text_color=(255, 255, 255)):
    font = pygame.font.SysFont("Arial", 40)
    text_render = font.render(text, 1, text_color)
    x, y, w, h = text_render.get_rect()
    x, y = position
    # pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    # pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    # pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    # pygame.draw.line(screen, (50, 50, 50), (x + w, y+h), [x + w, y], 5)
    # pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    pygame.draw.circle(screen, color,
                       (x + (w // 2), y + (h // 2)), 90, 0)
    return screen.blit(text_render, (x, y))


up_text_to_display = ""

while not done:
    # Check If Won Or Not
    check_is_win = a.is_win()
    if check_is_win == 1:
        done = True
        WON = True
    elif check_is_win == -1:
        done = True

    # Make Screen White
    screen.fill((255, 255, 255))

    # Set Color Lines
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    # # Draw Lines
    # for i in range(1, 9):
    #     pygame.draw.line(screen, BLACK, (i * 100, 0), (i * 100, 700), 4)
    # for i in range(1, 8):
    #     pygame.draw.line(screen, BLACK, (0, i * 100), (800, i * 100), 4)

    if up_text_to_display:
        font = pygame.font.SysFont(None, 64)
        img = font.render(up_text_to_display, True, BLACK)
        screen.blit(img, (300, 20))

    rock_button = button(screen, [100, 200], "Rock", (0, 255, 0))
    paper_button = button(screen, [350, 200], "Paper", (255, 0, 0))
    sc_button = button(screen, [600, 200], "Scissors", (0, 0, 255))

    pygame.display.flip()

pygame.quit()
