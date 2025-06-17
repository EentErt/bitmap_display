def analyze(data):
    '''Analyze the bitmap header to get file data.'''

    # Header starts with BM (0x424d)
    if not data.startswith('424d'):
        raise ValueError("File is not a bitmap file.")
    data = data[2:]
    file_size = int(data[0:8], 16)
    print (f"file size is {file_size} bytes")



#def hex_to_values(data):
