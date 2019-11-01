import sys
def print_lol(movies, indent=False, level=0,fname=sys.stdout):

    for moive in movies:

        if isinstance(moive, list):
           print_lol(moive, indent, level+1, fname)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end="", file=fname)
            print(moive, file=fname)
