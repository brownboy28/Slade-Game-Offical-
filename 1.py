else:
    print("ERROR \n Incorrect input \n Restart program to play again")

while count > 500:
    print("You escaped")

    if start == "2":
    # highscores insert here

    hisc = open("highscore.txt", "w+")
    highscore = hisc.read()
    highscore_in_no = int(highscore)
    if current_score > highscore_in_no:
        hisc.write(str(current_score))
        highscore_in_no = current_score

    print("Slade got you\n GAME OVER", count, "points")
    hisc.write(str(user + "-" + str(count) + "\n"))
    quit()

    if c2 == "2":
        print("Get sent to the headmaster's office for disrupting the lesson. \n -25 points")
    c3 = input("After a caning, you get let out for break,"
               "where do you go? \n 1-Libary 2-Playground")