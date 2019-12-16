import pickle
from class_test import AthlateList

def get_file(file_name):
    try:
        with open(file_name) as ff:
            data = ff.readline()
        temp_list = data.split(',')
        return(AthlateList(temp_list.pop(0),temp_list.pop(0),temp_list))
    except:
        print('File not found~')

def put_to_store(file_list):
    all_athletes = {}
    for each in file_list:
        ath = get_file(each)
        all_athletes[ath.name] = ath

    try:
        with open('All.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except:
        print('pickle error~')
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('All.pickle','rb') as pf:
            all_athletes = pickle.load(pf)
    except :
        print("pickle load error.")
    return all_athletes

put_to_store(['lily.txt','james0.txt'])
alla = get_from_store()
for athlete in alla:
    print(alla[athlete].name + " " + alla[athlete].dob + str(alla[athlete].top_3()))
