#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific index in a list.
    If idx is negative or out of range, returns the same list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Shift all elements after idx to the left
    for i in range(idx, len(my_list) - 1):
        my_list[i] = my_list[i + 1]
    # Remove the last element (duplicate after shifting)
    my_list[:] = my_list[:-1]
    return my_list
