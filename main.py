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
        List.append(gameclass.game(i + 1))
        if List[i].quit == True:
            break
    timePassed = time.time() - startTime
    print(f"Time taken{timePassed}")


if __name__ == "__main__":#selection
    main()