import time


def point1(direc):
    Input = input("What Direction do you want to move in")
    if Input.upper() == direc:  # selection sanitising
        time.sleep(1)
        print("Well done moving to Stage 2 Point 2")
        return 5
    else:
        time.sleep(1)
        print("Try again")
        return point1()



def point2():
    Input = input("""(Point 2)What Direction do you want to move in""")

    if "D" in Input.upper():  # selection sanitising
        print("Well done completed game")
        return 6
    else:
        time.sleep(1)
        print("Try again")
        return point2()