import os
from classes import *

a = Game()
while True:
    user_selected = input("Choose (Rock/Paper/Scissors) : ")
    os.system("cls")
    if user_selected.lower().strip() in ["rock", "paper", "scissors"]:
        ans = a.play_round(user_selected)
        print(f"BOT SELECTED -> {ans[1]}")
    else:
        print("You Did Not Select A Valid Option :(")
        continue
    a.show_status()
