import time


count = 100

start = input("Welcome to Reign of Terror \n 1-Start Game 2-Highscores")
if start == "2":

    hisc = open("highscore.txt", "a+")
    hisc.write(str(count) + "\n")


