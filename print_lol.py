def print_lol(movies, level):

    for moive in movies:

        if isinstance(moive, list):
           print_lol(moive, level+1)
        else:
            for tab_stop in range(level):
                print("\t", end="")
            print(moive)
