def print_lol(movies, indent=False, level=0):

    for moive in movies:

        if isinstance(moive, list):
           print_lol(moive, indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end="")
            print(moive)
