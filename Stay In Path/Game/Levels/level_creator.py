import pickle


class Level:
    def __init__(self, x, y):
        self.screen_x = (x * 100)
        self.screen_y = (y * 100)
        self.game_map = [[0 for _ in range(y)] for _ in range(x)]

    def make_wall(self):
        for c, i in enumerate(self.game_map[0]):
            self.game_map[0][c] = -1
        for c, i in enumerate(self.game_map[-1]):
            self.game_map[-1][c] = -1
        for c, i in enumerate(self.game_map):
            self.game_map[c][0] = -1
            self.game_map[c][-1] = -1

    def full(self, x, y):
        if type(x) == int and type(y) == int:
            self.game_map[x][y] = -1
        elif type(x) == list and type(y) == int:
            for i in x:
                self.game_map[i][y] = -1
        elif type(x) == int and type(y) == list:
            for i in y:
                self.game_map[x][i] = -1
        elif type(x) == list and type(y) == list:
            for i in x:
                for j in y:
                    self.game_map[i][j] = -1
        else:
            raise TypeError("Unknown Type. Values Must Be Int Or List.")

    def gamer_location(self, x, y):
        self.gamer_x = x
        self.gamer_y = y
        self.game_map[x][y] = 2
    
    def load_level(self,file_name):
        f = open(file_name,"rb")
        obj = pickle.load(f)
        f.close()
        # Load Game Map
        try:
            self.game_map = obj["game_map"]
        except:
            print("Error In Load Game Map")

        # Load Screen Width And Height
        try:
            self.screen_x = obj["screen_x"]
        except:
            print("Error In Load Screen X")
        try:
            self.screen_y = obj["screen_y"]
        except:
            print("Error In Load Screen Y")
            
        # Load Gamer X And Y
        try:
            self.gamer_x = obj["gamer_x"]
        except:
            print("Error In Load Gamer X")
        try:
            self.gamer_y = obj["gamer_y"]
        except:
            print("Error In Load Gamer Y")
            
        # Load Ball Color
        try:
            self.ball_color = obj["ball_color"]
        except:
            print("Error In Load Ball Color")
    
    def set_ball_color(self,RGB = (0,0,255)):
        self.ball_color = RGB

    def save(self, name):
        f = open(name, "wb")
        data = {}
        data["game_map"] = self.game_map
        data["screen_x"] = self.screen_x
        data["screen_y"] = self.screen_y
        data["gamer_x"] = self.gamer_x
        data["gamer_y"] = self.gamer_y
        data["ball_color"] = self.ball_color
        pickle.dump(data, f)
        f.close()
