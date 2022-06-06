from classes import *

circle = False
circle_x = 0
circle_y = 0
conf = Config(angle=9, cell_size=70, circle_radius=15, font_size=30)
done = False
turn = False
conf.define_labels(username_1, username_2)
conf.customize_score_text("[label0] ([score0]) VS [label1] ([score1])")
conf.move_score_text(-70, 0)

while not done:

    screen.fill((255, 255, 255))

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    conf.draw_map()

    if conf.circle:
        conf.update_circle()

    conf.draw_marked_pos()
    conf.draw_scores()

    for event in pygame.event.get():
        if event.type == 4:
            x, y = conf.find_position(event.pos[0], event.pos[1])
            if conf.is_in_screen(x, y):
                if conf.is_marked_pos(x, y) == -1:
                    conf.circle = True
                    conf.circle_x = x
                    conf.circle_y = y
                    conf.update_circle()
        elif event.type == 12:
            done = True
        elif event.type == 5:
            if conf.is_marked_pos(x, y) == -1:
                conf.mark_here(index=int(turn), turn=int(turn))
                conf.count_scores()
                conf.update_scores()
                turn = not turn
        else:
            pass

    winner = conf.is_game_finished()
    if winner != -1:
        from tkinter import *
        from tkinter import messagebox
        Tk().wm_withdraw()
        if winner != 3:
            messagebox.showinfo('', f'{winner} Won The Game !')
        else:
            messagebox.showinfo('', f'The Game Was TIE !')
        break
    pygame.display.flip()

pygame.quit()
