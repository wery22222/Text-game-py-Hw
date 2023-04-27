###############This file mainly calls functions from other modules################

#####imports#######
import gameclass
import time
##class create game class
def main():#method
    List = []#List/vector etc.
    i = -1
    startTime = time.time()
    while True:#iteration
        i+=1
        List.append([gameclass.game(i + 1), time.time()])
        if List[i].quit == True:
            break
    timePassed = time.time() - startTime
    for i in List:
        print(f"List of times {i[1]} in game {i[0]}")
    print(f"Time taken{timePassed}")


if __name__ == "__main__":#selection
    main()
