#!/usr/bin/python3

"""function that returns the JSON representation of an object (string) """
import json


def to_json_string(my_obj):
    """function that returns the JSON representation
    of an object (string)
    Args:
        my_obj (object): the object to load with json
    Returns:
        the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
