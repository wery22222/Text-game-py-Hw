import time


#defining all the game point functions
def point1(direc):
  Input = input("What Direction do you want to move in")
  if Input.upper() == direc:  # selection sanitising
    time.sleep(1)
    print("Well done moving to Stage 1 Point 2")
    return 1
  else:
    time.sleep(1)
    print("Try again")
    return point1(direc)


def point2():
  Input = input("""(Point 2)What Direction do you want to move in
You see a trap door above and below""")
  if Input.upper() == "N":  # selection sanitising
    time.sleep(1)
    print("Well done moving to Stage 2 Point 1")
    return 2
  else:
    time.sleep(1)
    print("Try again")
    return point2()


def point3(direc):
  Input = input("What Direction do you want to move in")
  if Input.upper() == direc:  # selection sanitising
    time.sleep(1)
    print("Well done moving to Stage 2 Point 2")
    return 3
  else:
    time.sleep(1)
    print("Try again")
    return point1(direc)


def point4():
  Input = input("""(Point 2)What Direction do you want to move in
You see a door North and East (Only directions)
Or are they?""")
  if Input.upper() == "W":  # selection sanitising
    time.sleep(1)
    print("Well done moving to Stage 3 Point 1")
    return 4
  else:
    time.sleep(1)
    print("Try again")
    return point2()


def point5(direc):
  Input = input("What Direction do you want to move in")
  if Input.upper() == direc:  # selection sanitising
    time.sleep(1)
    print("Well done moving to Stage 2 Point 2")
    return 5
  else:
    time.sleep(1)
    print("Try again")
    return point1()


def point6():
  Input = input("""(Point 2)What Direction do you want to move in""")

  if "D" in Input.upper():  # selection sanitising
    print("Well done completed game")
    return 6
  else:
    time.sleep(1)
    print("Try again")
    return point2()
