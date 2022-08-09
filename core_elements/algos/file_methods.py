import json


def read_json_file(file_name):
    with open(file_name, "r") as read_file:
        return json.load(read_file)
