import os
import pickle
from print_lol import print_lol

man = []
oman = []
try:
    with open("yuming.txt", 'r') as data3:
        for line in data3:
            try:
                (whos, says) = line.split(":", 1)
                if whos == "A":
                    man.append(says)
                elif whos == "B":
                    oman.append(says)
                else:
                    print("no A or B")
            except:
                print("No man or oman.")
except IOError as err:
    print("File error: " + str(err))


try:
    with open('man_data', 'wb') as man_file, open('oman_data', 'wb') as oman_file:
        pickle.dump(man,man_file)
        pickle.dump(oman,oman_file)
except IOError as err:
    print('pickle error' + str(err))

try:
    with open('man_data', 'rb') as man_refile, open("oman_data", 'rb') as oman_refile:
        A_says = pickle.load(man_refile)
        B_syas = pickle.load(oman_refile)
        print_lol(man, A_says)
        print_lol(oman, B_syas)
except :
    print('refile faild')
