import os
rep_word = "B"
data1 = open('yuming.txt', mode='r',  encoding='utf-8')
data_new = open('yuming2.txt', mode='w', encoding='utf-8')
for line in data1:
    if rep_word in line:
        line = line.replace(rep_word, rep_word+" SAID")

    data_new.write(line)
    data_new.flush()

data_new.close()
data1.close()
