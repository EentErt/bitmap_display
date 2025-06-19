from char_map import get_char_map
import copy
import math

class ArrayObject():
    def __init__(width, height, array):
        self.width = width
        self.height = height
        self.array = array

class PixelArray():
    def __init__(self, width, height, value_array):
        self.display = "VALUE"
        self.depth = 0 # The depth of current collapse. 0 = raw pixel data, 1 = pixel pairs, n = 2+ -> clusters of size 2 ^ n
        self.width = width
        self.char_width = self.width
        self.height = height
        self.value_array_original = value_array
        self.value_array = copy.deepcopy(value_array)
        self.black = 0
        self.white = 255
        self.gray = 127
        self.compression = 0
        self.normalize()
        self.list_array = [] # A list of lists of pixels as clusters
        self.combine()
        self.collapse()
        self.char_array = []
        self.list_array_to_char_array(self.display)

    # normalize values
    def normalize(self, black=0, white=255, gray=127):
        for i in range(len(self.value_array)):
            for j in range(len(self.value_array[i])):
                if self.value_array[i][j] >= white:
                    self.value_array[i][j] = 1
                elif self.value_array[i][j] <= black:
                    self.value_array[i][j] = 0
                elif self.value_array[i][j] >= gray:
                    self.value_array[i][j] = 1
                else:
                    self.value_array[i][j] = 0
        #self.value_array = list(map(lambda y: list(map(lambda x: round(x / 255), y)), self.value_array))

    # combine pixels into pixel pairs because console characters are 2 high and 1 wide
    def combine(self):
        self.list_array = []
        self.depth += 1
        for i in range(0, len(self.value_array), 2):
            # For every two rows, add a list to list_array
            self.list_array.append([])
            for j in range(len(self.value_array[i])):
                if i+1 == len(self.value_array):
                    self.list_array[i//2].append((self.value_array[i][j], 0,))
                else:
                    self.list_array[i//2].append((self.value_array[i][j], self.value_array[i+1][j],))

    # collapse pixel pairs into pixel clusters
    def collapse(self):
        new_array = []
        for i in range(0, len(self.list_array), 2):
            new_array.append([])
            for j in range(0, len(self.list_array[i]), 2):
                pair_1 = self.list_array[i][j]
                if i+1 == len(self.list_array) and j+1 == len(self.list_array[i]):
                    pair_2 = (0, 0,)
                    pair_3 = (0, 0,)
                    pair_4 = (0, 0,)
                if i+1 < len(self.list_array):
                    pair_2 = self.list_array[i+1][j]
                if j+1 < len(self.list_array[i]):
                    pair_3 = self.list_array[i][j+1]
                if i+1 < len(self.list_array) and j+1 < len(self.list_array[i]):
                    pair_4 = self.list_array[i+1][j+1]
                cluster = pair_1 + pair_2 + pair_3 + pair_4
                new_array[i//2].append(cluster)
        self.depth += 1
        self.list_array = new_array
    
    # compress 4 values into a single value to reduce image size
    def compress(self, depth):
        if depth == 0:
            return
        if len(self.value_array) <=2 or len(self.value_array[0]) <= 2:
            raise Exception("image can not be compressed further")
        while depth > 0:
            print("Compressing")
            new_value_array = []
            for i in range(0, len(self.value_array), 2):
                new_value_array.append([])
                for j in range(0, len(self.value_array[i]), 2):
                    if i + 1 < self.height and j + 1 < self.width:
                        new_value_array[i//2].append((self.value_array[i][j] + self.value_array[i+1][j] + self.value_array[i][j+1] + self.value_array[i+1][j+1]) // 4)
                    elif i + 1 < self.height and j + 1 == self.width:
                        new_value_array[i//2].append((self.value_array[i][j] + self.value_array[i+1][j]) // 2)
                    elif i + 1 == self.height and j + 1 < self.width:
                        new_value_array[i//2].append((self.value_array[i][j] + self.value_array[i][j+1]) // 2)
                    else:
                        new_value_array[i//2].append(self.value_array[i][j])
            self.value_array = new_value_array
            if self.width % 2 == 0:
                self.width /= 2
            else:
                self.width = self.width // 2 + 1
            if self.height % 2 == 0:
                self.height /= 2
            else:
                self.height = self.height // 2 + 1
            self.compression += 1
            depth -= 1
        self.refresh()

    # expand by rebuilding the array at a lower compression level, if depth = 0, rebuild at full size
    def expand(self, depth = 1):
        if self.compression == 0:
            raise Exception("Image is full size and can not be expanded further.")
        if depth == 0:
            self.compression = 0
        else:
            self.compression -= depth
        self.renew()

    # convert pixel clusters into characters
    def list_array_to_char_array(self, output_type):
        for i in range(len(self.list_array)):
            self.char_array.append("")
            for cluster in self.list_array[i]:
                char = get_char_map(output_type, cluster)
                if char is None:
                    char = get_char_map("VALUE", (sum(cluster) / len(cluster))//.25)
                self.char_array.append(char)          
            self.char_array.append("\n")
        self.depth += 1

    # rebuild character_array
    def refresh(self):
        self.depth = 0
        self.combine()
        self.collapse()
        self.char_array = []
        self.list_array_to_char_array(self.display)

    # rebuild list_array
    def renew(self):
        self.value_array = copy.deepcopy(self.value_array_original)
        self.normalize(self.black, self.white, self.gray)
        compression = self.compression
        self.compression = 0
        self.compress(compression)
        self.refresh()

    # set a level
    def set_level(self, level, value):
        value = int(value)
        if level == "BLACK":
            if value >= self.gray or value >= self.white:
                raise ValueError(f"Black level must be below gray({self.gray}) and white({self.white}) levels")
            self.black = value
        elif level == "WHITE":
            if value <= self.black or value <= self.gray:
                raise ValueError(f"White level must be above gray({self.gray}) and white({self.white}) levels")
            self.white = value
        else:
            if value <= self.black or value >= self.white:
                raise ValueError(f"Gray level must be between black({self.black}) and white({self.white}) levels")
            self.gray = value
        self.renew()

    # return size of the output (width, height)
    def get_size(self):
        return len(self.list_array[0]), len(self.list_array)

    # set the display mode
    def set_display_mode(self, mode):
        if mode == "VALUE" or mode == "DOTS" or mode == "CHARACTERS":
            self.display = mode
            self.refresh()
        else:
            raise ValueError(f'Unrecognized display type "{mode.lower()}"')

    def __repr__(self):
        if self.depth == 0:
            return str(self.value_array)
        elif self.depth == 1:
            return str(self.list_array)
        else:
            return ''.join(self.char_array)