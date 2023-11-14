#!/usr/bin/python3
'''task 7 module'''


from sys import argv
from os.path import exists


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []
my_list.extend(argv[1:])
save_to_json_file(my_list, filename)
