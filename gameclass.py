###Imports###
import stage1.point1
import stage1.point2
import stage1.point3

import random, time
def function_caller(p):
    direc = "NESWUD"
    p += 1
    if p == 1:
        return stage1.point1.point1(random.choice(direc))
    elif p == 2:
        return stage1.point1.point2()
    elif p == 3:
        return stage1.point2.point1(random.choice(direc))
    elif p == 4:
        return stage1.point2.point2()
    elif p == 5:
        return stage1.point3.point1(random.choice(direc))
    elif p == 6:
        return stage1.point3.point2()


class game:  # class
    def __init__(self, game_number):  # method
        self.tempList = [0, 1]
        self.point = 0
        self.gameNumber = game_number
        self.quit = False
        if game_number != 1:
            self.call_parts()
        else:
            if self.input_handler_start() == 3:
                self.quit = True

    def call_parts(self):  # method
        while self.point < 6 and self.quit is not True:  # iteration
            print(f"{self.point} HA")
            self.point = function_caller(self.point)
        else:
            self.quit = True

    def input_handler_start(self):  # Method
        theInput = input("""You are playing a game
the only way to escape it past this
is to complete it (q) else type 
Start(S) or help(h) for new player""")
        if theInput.upper() == "Q":  # selection sanitising
            print("Quiting")
            return 3
        elif theInput.upper() == "S" or theInput.upper() == "START" or "" == theInput.upper():  # selection sanitising
            print("Starting")
            self.call_parts()
            return 1
        elif theInput.upper() == "H" or theInput.upper() == "HELP":  # selection sanitising
            print("""You can move (N,E,S,W,U,D)""")
            self.call_parts()
            return 1
