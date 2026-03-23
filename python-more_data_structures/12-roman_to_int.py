#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    i = 0
    while i < len(roman_string):
        current = roman_map.get(roman_string[i], 0)
        if i + 1 < len(roman_string):
            next_val = roman_map.get(roman_string[i + 1], 0)
            if current < next_val:
                total += next_val - current
                i += 2
                continue
        total += current
        i += 1

    return total
