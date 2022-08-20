import json


def read_json_file(file_name):
    with open(file_name, "r") as read_file:
        return json.load(read_file)


def overwrite_json_file(file_name, dict_to_dump):
    with open(file_name, "w", encoding='utf-8') as json_file:
        json.dump(dict_to_dump, json_file)
