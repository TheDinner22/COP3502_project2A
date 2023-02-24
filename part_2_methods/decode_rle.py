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
