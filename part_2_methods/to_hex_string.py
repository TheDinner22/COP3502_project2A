# I copied this code from my lab4 code
#
# convert a decimal number to hex
# using acsii MAGIC!
#
# TYPE:
# - number is an int (positive)
# - returns a string (hex repr. of number)
def decimal_to_hex(number):
    hex = ""

    while number != 0:
        remainder = number % 16

        if remainder < 10:
            # 48 just so happens to be the number we have to add
            # to get to the ascii representation of a number
            # chr(48) is '0', etc
            hex += chr(remainder + 48)
        else:
            # I have no idea why this works with 55 instead of 54,
            # but it does
            hex += chr(remainder + 55)

        number //= 16

    # reverse the order and return
    return hex[::-1]

# Translates data (RLE or raw) a hexadecimal string (without delimiters). This method can also aid debugging. 
# Ex: to_hex_string([3, 15, 6, 4]) yields string "3f64". 
def to_hex_string(data):
    # TODO is there a difference between RLE or raw?
    # TODO can I assume that every item in data is <=15?
    hex = ""

    # map over every item, converting the decimal to hex
    for item in data:
        hex += decimal_to_hex(item)

    # example wants lowercase so that is what we return
    return hex.lower()
