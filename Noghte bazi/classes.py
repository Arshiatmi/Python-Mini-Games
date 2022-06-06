import pygame


username_1 = input("Enter Player 1 Name (Red) : ")
username_2 = input("Enter Player 2 Name (Green) : ")
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1000, 700))
score_instances = []


class Mark:
    def __init__(self, pos, color, turn, x, y):
        self.turn = turn
        self.pos = pos
        self.color = color
        self.x = x
        self.y = y


class Score:
    def __init__(self, color, x, y, size):
        self.color = color
        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x * self.size,
                                              self.y * self.size, self.size, self.size))


class Config:
    def __init__(self, angle=9, cell_size=100, circle_radius=25, font_size=30):
        global screen
        self.circle = False
        self.circle_x = 0
        self.circle_y = 0
        self.colors = {"BLACK": (0, 0, 0), "RED": (
            255, 0, 0), "GREEN": (0, 255, 0), "BLUE": (0, 0, 255)}
        self.circle_color = self.colors["BLUE"]
        self.circle_radius = circle_radius
        self.mark_colors = [self.colors["RED"], self.colors["GREEN"]]
        self.marked_pos = []
        self.scores = [0, 0]
        self.map_x = angle
        self.map_y = angle - 1
        self.labels = ["", ""]
        self.map = [[-1 for _ in range(self.map_x + 1)]
                    for _ in range(self.map_y + 1)]
        self.cell_size = cell_size
        self.font_size = font_size
        self.font = pygame.font.SysFont(None, self.font_size)
        screen = pygame.display.set_mode(
            (self.map_x * self.cell_size + 300, self.map_y * self.cell_size))
        self.score_location = ((self.map_x * self.cell_size + 150 -
                                (self.cell_size // 4 * 3), self.map_y * self.cell_size // 2 - 10))

    def define_labels(self, label_1, label_2):
        self.labels = [label_1, label_2]

    # Format : some text [var]
    # Variables :
    #       score0
    #       score1
    #       label0
    #       label1
    def customize_score_text(self, format):
        self.text_format = format

    def is_game_finished(self):
        if len(self.marked_pos) >= (self.map_x * (self.map_y + 1)):
            if self.labels[0] and self.labels[1]:
                if self.scores[0] > self.scores[1]:
                    return self.labels[0]
                elif self.scores[0] == self.scores[1]:
                    return 3
                else:
                    return self.labels[1]
            else:
                if self.scores[0] > self.scores[1]:
                    return 0
                elif self.scores[0] == self.scores[1]:
                    return 3
                else:
                    return 1
        return -1

    def draw_map(self):
        for i in range(1, self.map_y + 1):
            pygame.draw.line(screen, self.colors["BLACK"], (
                i * self.cell_size, 0), (i * self.cell_size, self.map_y * self.cell_size), 4)
        for i in range(1, self.map_x):
            pygame.draw.line(screen, self.colors["BLACK"], (0, i * self.cell_size), ((
                self.map_x - 1) * self.cell_size, i * self.cell_size), 4)
        self.update_scores()

    def draw_marked_pos(self) -> None:
        for i in self.marked_pos:
            pygame.draw.circle(screen, i.color, i.pos, self.circle_radius)

    def move_score_text(self, x_move, y_move):
        x = self.score_location[0] + x_move
        y = self.score_location[1] + y_move
        self.score_location = [x, y]

    def __str__(self) -> str:
        if self.text_format:
            txt = self.text_format.replace("[score0]", str(self.scores[0]))
            txt = txt.replace("[score1]", str(self.scores[1]))
            txt = txt.replace("[label1]", self.labels[1])
            txt = txt.replace("[label0]", self.labels[0])
            return txt
        else:
            return self.labels[0] + "(" + str(self.scores[0]) + ")" + " Vs " + self.labels[1] + "(" + str(self.scores[1]) + ")"

    def update_circle(self, x=-1, y=-1) -> None:
        if x == -1:
            x = self.circle_x
        if y == -1:
            y = self.circle_y
        pygame.draw.circle(screen, self.circle_color,
                           (x, y), self.circle_radius)
        self.update_scores()

    def mark_here(self, color=[(255, 0, 0), (0, 255, 0)], index=0, turn=0) -> None:
        x, y = self.find_position(self.circle_x, self.circle_y)
        x //= self.cell_size
        y //= self.cell_size
        self.marked_pos.append(
            Mark([self.circle_x, self.circle_y], color[index], turn, x, y))
        self.map[x][y] = turn

    def is_marked_pos(self, x, y) -> int:
        for i in self.marked_pos:
            if list(i.pos) == [x, y]:
                return i.turn
        return -1

    def is_marked_pos_index(self, x, y) -> int:
        for i in self.marked_pos:
            if i.x == x and i.y == y:
                return i.turn
        return -1

    def get_score_from_house(self, x, y) -> int:
        h1 = self.is_marked_pos_index(x, y)
        h2 = self.is_marked_pos_index(x + 1, y)
        h3 = self.is_marked_pos_index(x, y + 1)
        h4 = self.is_marked_pos_index(x + 1, y + 1)
        if h1 == h2 and h2 == h3 and h3 == h4 and h4 != -1:
            score_instances.append(
                Score(self.mark_colors[h1], x, y, self.cell_size))
            return h1
        else:
            return -1

    def count_scores(self) -> None:
        self.scores = [0, 0]
        for i in range(self.map_y):
            for j in range(self.map_x):
                sc = self.get_score_from_house(i, j)
                if sc != -1:
                    self.scores[sc] += 1

    def update_scores(self, text="", color=(0, 0, 0)) -> None:
        pos = self.score_location
        if text:
            txt = self.font.render(text, 1, color)
        else:
            txt = self.font.render(str(self), 1, color)
        screen.blit(txt, pos)

    def draw_scores(self):
        for i in score_instances:
            i.draw()

    def is_in_screen(self, x, y):
        x, y = self.find_position(x, y)
        if x >= (self.map_x * self.cell_size):
            return False
        elif y > (self.map_y * self.cell_size):
            return False
        return True

    def find_position(self, x, y) -> tuple:
        x /= self.cell_size
        y /= self.cell_size
        x = round(x) * self.cell_size
        y = round(y) * self.cell_size
        return x, y
