# Joe Goodman
# Project two part A
# 02/15/23

# reqs:
# standalone menu
# menu option one, two and six

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

# Returns number of runs of data in an image data set; double this result for length of encoded (RLE) list. 
# Ex: count_runs([15, 15, 15, 4, 4, 4, 4, 4, 4]) yields integer 2. 
# each item in falt_data represents a pixel on an image, the items value represents the pixel's color
def count_runs(flat_data):
    # iterate over each pixel and compare its color to the previous pixel's
    # color
    # if they are !=, add one to the counter
    prev = None
    counter = 0
    for pixel in flat_data:
        if pixel != prev:
            counter += 1 
        prev = pixel

    return counter

# Returns encoding (in RLE) of the raw data passed in; used to generate RLE representation of a data. 
# Ex: encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]) yields list [3, 15, 6, 4]. 
def encode_rle(flat_data):
    # if flat_data is empty, return an empty list
    if len(flat_data) == 0:
        return []

    rle_data = []
    current_run = {"value": flat_data[0], "length": 0 }
    for pixel in flat_data:
        # is this pixel part of the current run? (or is this the first iteration)
        if pixel == current_run["value"] or current_run["value"] == None:
            # increment the length of this run
            current_run["length"] += 1
        else:
            # if it's not, add the current run to rle_data
            rle_data.extend([current_run["length"], current_run["value"]])
            # and reset current_run
            current_run = {"value": pixel, "length": 1 }

    # the for loop has not added the last run to the rle_data
    # so I do that here
    rle_data.extend([current_run["length"], current_run["value"]])

    return rle_data

# Returns decompressed size RLE data; used to generate flat data from RLE encoding. (Counterpart to #2) 
# Ex: get_decoded_length([3, 15, 6, 4]) yields integer 9. 
def get_decoded_length(rle_data):
    pass

# Returns the decoded data set from RLE encoded data. This decompresses RLE data for use. (Inverse of #3) 
# Ex: decode_rle([3, 15, 6, 4]) yields list [15, 15, 15, 4, 4, 4, 4, 4, 4, 4]. 
def decode_rle(rle_data):
    pass

# Translates a string in hexadecimal format into byte data (can be raw or RLE). (Inverse of #1) 
# Ex: string_to_data ("3f64") yields list [3, 15, 6, 4]. 
def string_to_data(data_string):
    pass

# Translates  RLE data into  a human-readable representation.  For  each  run,  in  order,  it should  display  the  run 
# length in decimal (1-2 digits); the run value in hexadecimal (1 digit); and a delimiter, ‘:’, between runs. (See 
# examples in standalone section.) 
# Ex: to_rle_string([15, 15, 6, 4]) yields string "15f:64". 
def to_rle_string(rle_data):
    pass

# Translates a string in human-readable RLE format (with delimiters) into RLE byte data. (Inverse of #7) 
# Ex: string_to_rle("15f:64") yields list [15, 15, 6, 4].
def string_to_rle(rle_string):
    pass

# code from lab4
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

def error(msg):
    raise Exception(msg)

def main():
    pass

def tests():
    assert to_hex_string([3, 15, 6, 4]) == "3f64"
    assert count_runs([15, 15, 15, 4, 4, 4, 4, 4, 4]) == 2
    assert encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]) == [3, 15, 6, 4]

if __name__ == "__main__":
    tests()
