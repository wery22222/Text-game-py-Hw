###Imports###
import stage1 as st1

import random, time


def function_caller(p):
  direc = "NESWUD"
  p += 1
  if p == 1:
    return st1.point1(random.choice(direc))
  elif p == 2:
    return st1.point2()
  elif p == 3:
    return st1.point3(random.choice(direc))
  elif p == 4:
    return st1.point4()
  elif p == 5:
    return st1.point5(random.choice(direc))
  elif p == 6:
    return st1.point6()


class game:  # class

  def __init__(self, game_number):  # constructor method
    # Defining all the member variables
    self.point = 0
    self.gameNumber = game_number
    self.quit = False
    #Checks wether 1st game
    if game_number != 1:
      self.call_parts()
    else:
      if self.input_handler_start() == 3:
        self.quit = True

  def call_parts(self):  # method
    while self.point < 6 and self.quit is not True:  # iteration
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
    elif theInput.upper() == "S" or theInput.upper(
    ) == "START" or "" == theInput.upper():  # selection sanitising
      print("Starting")
      self.call_parts()
      return 1
    elif theInput.upper() == "H" or theInput.upper(
    ) == "HELP":  # selection sanitising
      print("""You can move (N,E,S,W,U,D)""")
      self.call_parts()
      return 1
