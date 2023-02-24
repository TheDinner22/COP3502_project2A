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

