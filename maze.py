class Maze:
    def __init__(self, filepath):
        self.map = []
        self.start = None
        self.end = None
        self.load_maze(filepath)

    # Get all attributes
    def load_maze(self, filepath):
        try:
            with open(filepath, 'r') as file:
                for row_index, line in enumerate(file):
                    line = line.strip('\n')
                    row = list(line)
                    self.map.append(row)
                    for col_index, char in enumerate(row):
                        if char == 'S':
                            self.start = (row_index, col_index)
                        elif char == 'E':
                            self.end = (row_index, col_index)
        except Exception:
            print("Load Maze failure...")

    # The method of display
    def print_maze(self, player_pos=None):
        for i, row in enumerate(self.map):
            row_str = ""
            for j, cell in enumerate(row):
                if player_pos and (i, j) == player_pos:
                    row_str += "P"
                else:
                    row_str += cell
            print(row_str)

    # Judges a coordinate whether approved to move
    def is_walkable(self, row, col):
        if 0 <= row < len(self.map) and 0 <= col < len(self.map[0]):
            return self.map[row][col] != '#'
        return False
