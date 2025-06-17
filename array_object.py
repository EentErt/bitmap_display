from char_map import get_char_map
import math

class PixelArray():
    def __init__(self, width, height, value_array):
        self.status = "value array"
        self.depth = 0 # The depth of current collapse. 0 = raw pixel data, 1 = pixel pairs, n = 2+ -> clusters of size 2 ^ n
        self.width = width
        self.char_width = self.width
        self.height = height
        self.value_array = value_array
        self.normalize()
        self.list_array = [] # A list of lists of pixels as clusters
        self.collapse()
        self.char_array = [] # A list of strings representing the rows of the image
        self.list_array_to_char_array()

    def to_utf(self, depth):
        return

    # normalize values, this might not be needed.
    def normalize(self):
        self.value_array = list(map(lambda y: list(map(lambda x: round(x / 255), y)), self.value_array))
    '''
    def normalize(self):
        for i in range(self.width):
            for j in range(self.height):
                self.value_array[i][j] /= 255
                self.value_array[i][j] = round(self.value_array[i][j])
    '''
    
    # collapse pixels into pixel pairs because console characters are 2 high and 1 wide
    def collapse(self):
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
    def collapse_r(self):
        new_array = []
        for i in range(len(0, self.list_array, 2)):
            for j in range(len(0, self.list_array[i], 2)):
                new_array.append(self.list_array[i][j])
                new_array.append(self.list_array[i+1][j])
                new_array.append(self.list_array[i][j+1])
                new_array.append(self.list_array[i+1][j+1])
    



        
    
    def list_array_to_char_array(self):
        char_map = get_char_map(self.depth)
        for i in range(len(self.list_array)):
            self.char_array.append("")
            for pair in self.list_array[i]:
                self.char_array.append(char_map.get(pair))
            self.char_array.append("\n")
        self.depth += 1

    def __repr__(self):
        if self.depth == 0:
            return str(self.value_array)
        elif self.depth == 1:
            return str(self.list_array)
        else:
            return ''.join(self.char_array)