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
