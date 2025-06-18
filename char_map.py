def value_array_to_char_array(array):
    for row in array:
        char_string = ""
        for item in row:
            char_string += value_to_char(item)
        # print(char_string)

def value_to_char(value):
    if value < 255 / 3:
        return " "
    elif value > 255 * 2 / 3:
        return "\u2588"
    else:
        return "/"

def get_char_map(depth, cluster):
    if depth == "braille":
        return get_braille(cluster)
    char_dict = {
        0: {
            1: "\u2588",
            0: " "
        },
        1: {
            (1, 1,): "\u2588",
            (1, 0,): "\u2580",
            (0, 1,): "\u2584",
            (0, 0,): " "
        },
        2: {
            (1, 1, 1, 1, 1, 1, 1, 1,): "B", # ⣿
            (1, 1, 1, 1, 1, 1, 1, 0,): "9", # ⡿
            (1, 1, 1, 1, 1, 1, 0, 0,): "P", # ⡟
            (1, 1, 1, 1, 1, 1, 0, 1,): "R",
            (1, 1, 1, 1, 1, 0, 0, 0,): '\u0393',
            (1, 1, 1, 1, 1, 0, 0, 1,): '[',
            (1, 1, 1, 1, 1, 0, 1, 0,): 'F',
            (1, 1, 1, 1, 1, 0, 1, 1,): '\u0411',
            (1, 1, 1, 1, 0, 0, 0, 0,): '(',
            (1, 1, 1, 1, 0, 0, 0, 1,): 'L',
            (1, 1, 1, 1, 0, 0, 1, 0,): '{',
            (1, 1, 1, 1, 0, 0, 1, 1,): 'b',
            (1, 1, 1, 1, 0, 1, 0, 0,): 'f',
            (1, 1, 1, 1, 0, 1, 0, 1,): '\u00A3',
            (1, 1, 1, 1, 0, 1, 1, 0,): '\u00FE',
            (1, 1, 1, 1, 0, 1, 1, 1,): '\u2422',
            (1, 1, 1, 0, 0, 0, 0, 0,): '\u05F3',
            (1, 1, 1, 0, 0, 0, 0, 1,): '\u0661',
            (1, 1, 1, 0, 0, 0, 1, 0,): '\u0661',
            (1, 1, 1, 0, 0, 0, 1, 1,): '\u0196',
            (1, 1, 1, 0, 0, 1, 0, 0,): '\u06f6',
            (1, 1, 1, 0, 0, 1, 0, 1,): ' ', #####
            (0, 0, 0, 0, 1, 1, 1, 1,): "o",
            (0, 0, 1, 1, 1, 1, 0, 0,): "#",
            (1, 1, 0, 0, 0, 0, 1, 1,): "I", 
            (1, 0, 1, 0, 1, 0, 1, 0,): "O", 
            (0, 1, 0, 1, 0, 1, 0, 1,): "O",
            (0, 1, 0, 1, 1, 0, 1, 0,): "-",
            (1, 1, 0, 0, 1, 1, 0, 0,): "|",
            (0, 0, 1, 1, 0, 0, 1, 1,): "|",
            (0, 0, 0, 0, 0, 0, 0, 0,): " "
        },
        "value": {
            0: " ",
            1: "\u2591",
            2: "\u2592",
            3: "\u2593",
            4: "\u2588"
        },
    }
    if cluster not in char_dict[depth]:
        return None
    return char_dict[depth].get(cluster)

def get_braille(eight_cluster):
    # braille is a binary representation of the number, starting at \u2800
    bit_string = ''.join(map(str, eight_cluster))
    return chr(ord("\u2800") + int(bit_string, 2))




