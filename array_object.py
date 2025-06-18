from char_map import get_char_map
import math

class ArrayObject():
    def __init__(width, height, array):
        self.width = width
        self.height = height
        self.array = array

class PixelArray():
    def __init__(self, width, height, value_array):
        self.status = "value array"
        self.depth = 0 # The depth of current collapse. 0 = raw pixel data, 1 = pixel pairs, n = 2+ -> clusters of size 2 ^ n
        self.width = width
        self.char_width = self.width
        self.height = height
        self.value_array = value_array
        self.compressed_array = []
        self.normalize()
        # self.compress(2)
        self.list_array = [] # A list of lists of pixels as clusters
        self.combine()
        self.collapse(4)
        self.char_array = [] # A list of strings representing the rows of the image
        self.list_array_to_char_array()

    def to_utf(self, depth):
        return

    # normalize values, this might not be needed.
    def normalize(self):
        self.value_array = list(map(lambda y: list(map(lambda x: round(x / 255), y)), self.value_array))

    
    # combine pixels into pixel pairs because console characters are 2 high and 1 wide
    def combine(self):
        self.depth += 1
        for i in range(0, len(self.value_array), 2):
            # For every two rows, add a list to list_array
            self.list_array.append([])
            for j in range(len(self.value_array[i])):
                if i == self.height - 1:
                    self.list_array[i//2].append((self.value_array[i][j], 0,))
                else:
                    self.list_array[i//2].append((self.value_array[i][j], self.value_array[i+1][j],))


    # collapse pixel pairs into pixel clusters
    def collapse(self, depth):
        new_array = []
        if depth == 0:
            return
        for i in range(0, len(self.list_array), 2):
            new_array.append([])
            for j in range(0, len(self.list_array[i]), 2):
                pair_1 = self.list_array[i][j]
                if i+1 == len(self.list_array) and j+1 == len(self.list_array[i]):
                    pair_2 = (0, 0,)
                    pair_3 = (0, 0,)
                    pair_4 = (0, 0,)
                if i+1 < len(self.list_array):
                    pair_3 = self.list_array[i+1][j]
                if j+1 < len(self.list_array[i]):
                    pair_2 = self.list_array[i][j+1]
                if i+1 < len(self.list_array) and j+1 < len(self.list_array[i]):
                    pair_4 = self.list_array[i+1][j+1]
                cluster = pair_1 + pair_2 + pair_3 + pair_4
                new_array[i//2].append(cluster)
        self.depth += 1
        self.list_array = new_array
    
    def compress(self, depth):
        # compress 4 values into a new value
        if depth == 0:
            return
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
            depth -= 1
        



        
    
    def list_array_to_char_array(self):
        char_map = get_char_map(self.depth)
        for i in range(len(self.list_array)):
            self.char_array.append("")
            for cluster in self.list_array[i]:
                if cluster in char_map:
                    self.char_array.append(char_map.get(cluster))
                else:
                    value = (sum(cluster) / len(cluster)) // 0.25
                    self.char_array.append(get_char_map("value").get(value))
            self.char_array.append("\n")
        self.depth += 1
        print(char_map)

    def __repr__(self):
        if self.depth == 0:
            return str(self.value_array)
        elif self.depth == 1:
            return str(self.list_array)
        else:
            return ''.join(self.char_array)