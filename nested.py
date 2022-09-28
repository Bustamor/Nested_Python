# # Nested Dictionaries and lists
#
# MAIN NUMBER 1 (parts 1-4)
# x = [ [5,2,3], [10,8,9] ]
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# from curses import keyname
# from multiprocessing.sharedctypes import Value


# z = [ {'x': 10, 'y': 20} ]


# 1 change the value of 10 in x to 15
# x = [ [5,2,3], [10,8,9]]
# x [1] [0] = 15
# print (x)

# 2 Change last name of student to Bryant
# students [0] ["last_name"] = 'Bryant'
# print (students)

# 3 Change "Messi" to "Andres"
# sports_directory ['soccer'] [0] = "Andres"
# print (sports_directory)

# 4 Change value of 20 to 30

# z [0] ["y"] = 30
# print (z)


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# MAIN NUMBER 2


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):
    for i in range(len(students)):
        print(students[i])
    return students[i]


print(iterateDictionary(students))

# Main Number 3
# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name,
# the function prints the value stored in that key for each dictionary.
# For example, iterateDictionary2('first_name', students) should output:
# list_of_dicts

# Jordan
# Rosdales
# mark
# kb


# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# iterate over that list
# def iterate_dictionary2(key,list_of_dicts):
#     #iterate over list of dictionaries
# for i in range(len(list_of_dicts)):
#     print(list_of_dicts[i][key])
# def iterate_dictionary2(key_name, some_list):
#     for players in some_list:
#         print(players[key_name])

# iterate_dictionary2("first_name", students)

# iterate_dictionary2("last_name", students)

# Main Number 4

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
#  prints the name of each key along with the size of its list,
# and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


def printInfo(some_dict):
    for key in some_dict.keys():
        print(f'{len(some_dict[key])} {key}')
        for element in some_dict[key]:
            print(element)


printInfo(dojo)
