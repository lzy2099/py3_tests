import os

# names = ['james.txt', 'julie.txt', 'mikey.txt', 'sarah.txt']
#############################################
########### 用函数 之前
# with open('james.txt') as james_file:
#     data = james_file.readline()
#     james = data.strip().split(',')
# with open('julie.txt') as julie_file:
#     data = julie_file.readline()
#     julie = data.strip().split(',')
# with open('mikey.txt') as mikey_file:
#     data = mikey_file.readline()
#     mikey = data.strip().split(',')
# with open('sarah.txt') as sarah_file:
#     data = sarah_file.readline()
#     sarah = data.strip().split(',')

### 用函数之后  ##
def get_file(file_name):
    try:
        with open(file_name) as ff:
            data = ff.readline()
        return data.split(',')
    except:
        print('error')
james = get_file('james.txt')
julie = get_file('julie.txt')
mikey = get_file('mikey.txt')
sarah = get_file('sarah.txt')

####################################
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins + "." + secs)


new_james = []
new_julie = []
new_mikey = []
new_sarah = []

new_james = sorted(set([sanitize(each_one) for each_one in james]))[:3]
new_julie = sorted(set([sanitize(each_one) for each_one in julie]))[:3]
new_mikey = sorted(set([sanitize(each_one) for each_one in mikey]))[:3]
new_sarah = sorted(set([sanitize(each_one) for each_one in mikey]))[:3]

new_names = [new_james, new_julie, new_mikey, new_sarah]

for new_name in new_names:
    print(new_name)

uniq_james = []
for i in new_james:
    if i not in uniq_james:
        uniq_james.append(i)
print(uniq_james[0:3])
