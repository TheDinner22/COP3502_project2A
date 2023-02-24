# Returns decompressed size RLE data; used to generate flat data from RLE encoding. (Counterpart to #2) 
# Ex: get_decoded_length([3, 15, 6, 4]) yields integer 9. 
def get_decoded_length(rle_data):
    # sum every other element in rle data
    return sum(rle_data[::2])
