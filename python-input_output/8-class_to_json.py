#!/usr/bin/python3
"""Class to JSON module"""


def class_to_json(obj):
    """Returns dictionary description of an object for JSON serialization"""
    return obj.__dict__
