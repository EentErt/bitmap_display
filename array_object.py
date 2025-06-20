from char_map import get_char_map
import copy
import math

class PixelArray():
    def __init__(self, width, height, value_array):
        self.display = "VALUE"
        self.depth = 0 # The depth of current collapse. 0 = raw pixel data, 1 = pixel pairs, n = 2+ -> clusters of size 2 ^ n
        self.width = width
        self.char_width = self.width
        self.height = height
        self.value_array_original = value_array
        self.value_array = copy.deepcopy(value_array)
        self.normal_array = 
        self.threshold = 127
        self.highlight = 255
        self.compression = 0
        self.normalize()
        self.list_array = [] # A list of lists of pixels as clusters
        self.combine()
        self.collapse()
        self.char_array = []
        self.list_array_to_char_array(self.display)

    # normalize values
    def normalize(self, threshold = 127):
        for i in range(len(self.value_array)):
            for j in range(len(self.value_array[i])):
                if self.value_array[i][j] >= threshold:
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
            print("Compressing...")
            new_value_array = []
            for i in range(0, len(self.value_array), 2):
                new_value_array.append([])
                for j in range(0, len(self.value_array[i]), 2):
                    new_value_array[i//2].append(self.compress_values(i, j))
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
    
    # helper function for compress
    def compress_values(self, i, j):
        pixel_values = [self.value_array[i][j]]
        if i + 1 < len(self.value_array):
            pixel_values.append(self.value_array[i+1][j])
        if j + 1 < len(self.value_array[i]):
            pixel_values.append(self.value_array[i][j+1])
        if i + 1 < len(self.value_array) and j + 1 < len(self.value_array[i]):
            pixel_values.append(self.value_array[i+1][j+1])
        
        # when compression takes place, an especially light pixel takes precedence to maintain detail
        average_value = sum(pixel_values) // len(pixel_values)
        for pixel_value in pixel_values:
            if pixel_value > self.highlight:
                return pixel_value
        return average_value
        
        
        '''
        if i + 1 < self.height and j + 1 < self.width:
            new_value_array[i//2].append((self.value_array[i][j] + self.value_array[i+1][j] + self.value_array[i][j+1] + self.value_array[i+1][j+1]) // 4)
        elif i + 1 < self.height and j + 1 == self.width:
            new_value_array[i//2].append((self.value_array[i][j] + self.value_array[i+1][j]) // 2)
        elif i + 1 == self.height and j + 1 < self.width:
            new_value_array[i//2].append((self.value_array[i][j] + self.value_array[i][j+1]) // 2)
        else:
            new_value_array[i//2].append(self.value_array[i][j])
        '''

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
        self.normalize(self.threshold)
        self.combine()
        self.collapse()
        self.char_array = []
        self.list_array_to_char_array(self.display)

    # rebuild list_array
    def renew(self):
        self.value_array = copy.deepcopy(self.value_array_original)
        compression = self.compression
        self.compression = 0
        self.compress(compression)
        self.refresh()

    # set the threshold level
    def set_threshold(self, value):
        value = int(value)
        if value <= 0 or value >= 255:
            raise ValueError(f"Threshold must be between 0 and 255")
        self.threshold = value
        self.renew()

    # set the highlight level
    def set_highlight(self, value):
        value = int(value)
        if value <= 0 or value >= 255:
            raise ValueError(f"Highlight value must be between 0 and 255")
        self.highlight = value
        self.renew()

    # return size of the output (width, height)
    def get_size(self):
        return len(self.value_array[0]), len(self.value_array)//2

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