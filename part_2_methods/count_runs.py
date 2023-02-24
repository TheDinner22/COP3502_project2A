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

