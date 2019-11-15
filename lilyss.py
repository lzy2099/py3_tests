import os
def get_file(file_name):
    try:
        with open(file_name) as ff:
            data = ff.readline()
            temp_list = data.split(',')
        return (
        {'name': temp_list.pop(0),
        'DateOfBirth': temp_list.pop(0),
        'times': str(sorted(set([sanitize(t) for t in temp_list]))[:3])}
        )
    except:
        print('File not found~')

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins + "." + secs)

lilyd = get_file('lily.txt')
print("Athlate: "+lilyd['name']+'\n'+ "DateOfBirth: "+lilyd['DateOfBirth'] +'\n'+ "Best_time: " +lilyd['times'])
