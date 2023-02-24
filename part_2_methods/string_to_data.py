# easy error messages
def error(msg):
    raise Exception(msg)

# take in a single hex char and return its decimal representation
def hex_char_to_decimal(hex_char):
    # make sure the char has length 1
    if len(hex_char) != 1:
        error(f"hex char should only have length 1, got {hex_char}")

    # make sure that it is uppercase
    hex_char = hex_char.upper()

    hex_decimal_map = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }

    # asssumes that the hex_char is valid
    return hex_decimal_map[hex_char]

# Translates a string in hexadecimal format into byte data (can be raw or RLE). (Inverse of #1) 
# Ex: string_to_data ("3f64") yields list [3, 15, 6, 4]. 
def string_to_data(data_string):
    raw_data = []
    for hex_char in data_string:
        raw_data.append(hex_char_to_decimal(hex_char))

    return raw_data
