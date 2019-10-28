def print_lol(movies):

    for moive in movies:

        if isinstance(moive, list):
           print_lol(moive)
        else:
            print(moive)
