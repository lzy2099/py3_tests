import os

data1 = open('yuming.txt', mode='r',  encoding='utf-8')
data_new = open('yuming2.txt', mode='w', encoding='utf-8')
for line in data1:
    if "A" in line:
        line = line.replace("A", "A Said: ")
    else:
        line = line.replace("B", "B Said: ")
    data_new.write(line)
    data_new.flush()

data_new.close()
data1.close()
