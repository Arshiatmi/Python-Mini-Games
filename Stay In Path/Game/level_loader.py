import pickle
import os

class Data:
    def __init__(self,file_name):
        print(os.getcwd())
        if "Levels" not in file_name:
            os.chdir("Levels")
        f = open(file_name,"rb")
        self.data = data = pickle.load(f)
        f.close()
    
    @property
    def game_map(self):
        return self.data["game_map"]
    
    @property
    def screen_x(self):
        return self.data["screen_x"]
    
    @property
    def screen_y(self):
        return self.data["screen_y"]
        
    @property
    def gamer_x(self):
        return self.data["gamer_x"]

    @property
    def gamer_y(self):
        return self.data["gamer_y"]

    @property
    def ball_color(self):
        return self.data["ball_color"]
