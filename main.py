###############This file mainly calls functions from other modules################

#####imports#######
import gameclass
##class create game class
def main():#method
    List = []#List/vector etc.
    i = -1
    while True:#iteration
        i+=1
        List.append(gameclass.game(i + 1))
        if List[i].quit == True:
            break
    print(f"Attempts taken{i+1}")



if __name__ == "__main__":#selection
    main()
