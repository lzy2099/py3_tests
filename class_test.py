import os

class AthlateList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__(self)
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top_3(self):
        return (sorted(set([sanitize(t) for t in self]))[:3])

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins + "." + secs)

def get_file(file_name):
    try:
        with open(file_name) as ff:
            data = ff.readline()
            temp_list = data.split(',')
        return(
            AthlateList(temp_list.pop(0),
            temp_list.pop(0),
            temp_list)
            )
    except:
        print('File not found~')

# a1 = get_file('lily.txt')
# a1.append('1.21')
# a1.extend(['0.12', '1.11'])
# print(a1.name,a1.dob,a1.top_3())
# print(a1)


# import os
# class Athlete:
#     def __init__(self, a_name, a_dob=None, a_times=[]):
#         self.name = a_name
#         self.dob = a_dob
#         self.times = a_times
#     def top_3(self):
#         return (sorted(set([sanitize(t) for t in self.times]))[:3])
#     def add_time(self, ntime):
#         return self.times.append(ntime)
#     def add_times(self, ntime_list):
#         return self.times.extend(ntime_list)
#
# def sanitize(time_string):
#     if '-' in time_string:
#         splitter = '-'
#     elif ':' in time_string:
#         splitter = ':'
#     else:
#         return (time_string)
#     (mins,secs) = time_string.split(splitter)
#     return(mins + "." + secs)
#
# def get_file(file_name):
#     try:
#         with open(file_name) as ff:
#             data = ff.readline()
#             temp_list = data.split(',')
#         return(
#             Athlete(temp_list.pop(0),
#             temp_list.pop(0),
#             temp_list)
#             )
#     except:
#         print('File not found~')
#
# a1 = get_file('lily.txt')
# a1.add_time('1.21')
# a1.add_times(['0.12', '1.11'])
# print(a1.name,a1.top_3())
