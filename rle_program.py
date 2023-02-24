# Joe Goodman
# Project two part B
# 02/15/23

# import the ConsoleGfx class
from console_gfx import ConsoleGfx 

# reqs part A:
# standalone menu
# menu options one, two, and six
# main shoud:
# 1. Display welcome message
# 2. Display color test ( ConsoleGfx.test_rainbow )
# 3. Display the menu
# 4. Prompt for input
# i also implemented some of the methods that are required

# reqs part B:
# impl these six methods:
# to_hex_string(data) 
# count_runs(flat_data) 
# encode_rle(flat_data) 
# get_decoded_length(rle_data) 
# decode_rle(rle_data) 
# string_to_data(data_string) 

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
#
# so there is an issue where there is a "longest possible run"
# hex encoded rle delegates 1 char to the length and 1 char to the encoded value
# if flat_data were 10000 1's, the number of runs would not be 1!
def count_runs(flat_data):
    if len(flat_data) == 0:
        return []

    # first run is created with the first pixel's value
    current_run = {"length": 1, "value": flat_data[0]}
    run_counter = 0

    for pixel in flat_data[1:]:
        # if this pixel is part of the current run OR this is the first iteration
        if pixel == current_run["value"]:
            # is the run full?
            if current_run["length"] == 15:
                # if so, increment run counter
                run_counter += 1
                # initilize new run with pixel
                current_run = {"length": 1, "value": pixel}
            else:
                # if not, then we can just
                # increase the length of the run
                current_run["length"] += 1
        # pixel marks the end of the current run
        else:
            # increment run counter
            run_counter += 1
            # initilize new run with pixel
            current_run = {"length": 1, "value": pixel}

    # the last run is not counted so I increment the run_counter here
    # to compensate
    run_counter += 1

    return run_counter 

# Returns encoding (in RLE) of the raw data passed in; used to generate RLE representation of a data. 
# Ex: encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]) yields list [3, 15, 6, 4]. 
#
# again I need to beware the fact that runs have a max length of 15
def encode_rle(flat_data):
    # if flat_data is empty, return an empty list
    if len(flat_data) == 0:
        return []

    rle_data = []
    current_run = {"value": flat_data[0], "length": 1 }
    for pixel in flat_data[1:]:
        # is this pixel part of the current run?
        if pixel == current_run["value"]:
            # is the current run full?
            if current_run["length"] == 15:
                # if it is, add the current run to rle_data
                rle_data.extend([current_run["length"], current_run["value"]])
                # and reset current_run with the current pixel
                current_run = {"value": pixel, "length": 1 }
            else:
                # if its not, we can just increment its length
                current_run["length"] += 1
        else:
            # if it's not, add the current run to rle_data
            rle_data.extend([current_run["length"], current_run["value"]])
            # and reset current_run with the current pixel
            current_run = {"value": pixel, "length": 1 }

    # the for loop has not added the last run to the rle_data
    # so I do that here
    rle_data.extend([current_run["length"], current_run["value"]])

    return rle_data

# Returns decompressed size RLE data; used to generate flat data from RLE encoding. (Counterpart to #2) 
# Ex: get_decoded_length([3, 15, 6, 4]) yields integer 9. 
def get_decoded_length(rle_data):
    # sum every other element in rle data
    return sum(rle_data[::2])

# Returns the decoded data set from RLE encoded data. This decompresses RLE data for use. (Inverse of #3) 
# Ex: decode_rle([3, 15, 6, 4]) yields list [15, 15, 15, 4, 4, 4, 4, 4, 4]. 
def decode_rle(rle_data):
    raw_data = []

    # moving window which contains 2 elements in the list
    # in this list [1, 2, 3, 4, 5, 6, 7, 8], the window would be
    # [1, 2], then [3, 4], then [5, 6] etc
    for encoded_length_index in range(0, len(rle_data), 2):
        encoded_length = rle_data[encoded_length_index]
        encoded_data = rle_data[encoded_length_index+1]

        # add the encoded data to raw_data length times
        for _ in range(encoded_length):
            raw_data.append(encoded_data)

    return raw_data

# Translates a string in hexadecimal format into byte data (can be raw or RLE). (Inverse of #1) 
# Ex: string_to_data ("3f64") yields list [3, 15, 6, 4]. 
def string_to_data(data_string):
    raw_data = []
    for hex_char in data_string:
        raw_data.append(hex_char_to_decimal(hex_char))

    return raw_data

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

# easy error messages
def error(msg):
    raise Exception(msg)

# print the welcome message
def welcome():
    print("Welcome to the RLE image encoder!")

def menu():
    print("")
    print("RLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")
    print("")

def menu_input():
    user_input = int(input("Select a Menu Option: "))

    # make sure the input is valid and if its not,
    # crash
    if user_input < 0 or user_input > 9:
        error(f"invalid menu input! GOT: {user_input}")

    return user_input

def main():
    # stores the currrent loaded image
    current_image = None

    # Display welcome message
    welcome()
    print("")

    # Display color test ( ConsoleGfx.test_rainbow )
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print("")

    while True:
        # Display the menu
        menu()

        # Prompt for input
        # TODO should this loop?
        user_selection = menu_input()

        # 0. Exit
        if user_selection == 0:
            return

        # 1. Load File 
        elif user_selection == 1:
            # get the filename from the user
            filename = input("Enter name of file to load: ")

            # load the file
            current_image = ConsoleGfx.load_file(filename)

        # 2. Load Test Image 
        elif user_selection == 2:
            current_image = ConsoleGfx.test_image
            print("Test image data loaded.")

        # 3. Read RLE String
        elif user_selection == 3:
            pass

        # 4. Read RLE Hex String
        elif user_selection == 4:
            pass

        # 5. Read Data Hex String
        elif user_selection == 5:
            pass

        # 6. Display Image 
        elif user_selection == 6:
            ConsoleGfx.display_image(current_image)

        # 7. Display RLE String
        elif user_selection == 7:
            pass

        # 8. Display Hex RLE Data
        elif user_selection == 8:
            pass

        # 9. Display Hex Flat Data
        elif user_selection == 9:
            pass

# the methods I am required to implement have
# sample inputs and outputs
# this function makes sure tha the functions behave as expected
def tests():
    # tests from the comments provided in the pdf
    assert to_hex_string([3, 15, 6, 4]) == "3f64"
    assert count_runs([15, 15, 15, 4, 4, 4, 4, 4, 4]) == 2
    assert encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]) == [3, 15, 6, 4]
    assert get_decoded_length([3, 15, 6, 4]) == 9
    assert get_decoded_length([7, 15, 7, 4]) == 14
    assert decode_rle([3, 15, 6, 4]) == [15, 15, 15, 4, 4, 4, 4, 4, 4]
    assert string_to_data ("3f64") == [3, 15, 6, 4]

    # tests from zybooks
    assert count_runs([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]) == 25
    assert count_runs([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7 ]) == 6

    assert encode_rle([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7]) == [2,4,15,1,15,1,5,1,1,8,1,7]
    assert encode_rle([1,2,3,4,1,2,3,4]) == [1,1,1,2,1,3,1,4,1,1,1,2,1,3,1,4]
    assert encode_rle([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == [2,4,15,1,15,1,5,1]
    assert encode_rle([4,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == [1,4,1,5,15,1,15,1,5,1]


if __name__ == "__main__":
    tests()
    main()
