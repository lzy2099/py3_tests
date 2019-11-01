import os
from print_lol import print_lol

maan = []
oather = []
try:
    with open("yuming.txt", "r") as data2:
        for num,line in enumerate(data2, 1):
            try:
                (auth, says) = line.split(":", 1)
                says = says.strip()
                if auth == "A":
                    maan.append(says)
                elif auth == "B":
                    oather.append(says)
            except ValueError as err:
                print("ValueError: " + str(err))

except IOError as err:
    print("File Error: " + str(err))
try:
    with open("A.txt", "w") as A, open("B.txt", "w") as B:
        print_lol(maan, fname=A)
        print_lol(oather, fname=B)

except IOError as err:
    print("File error." + str(err))
