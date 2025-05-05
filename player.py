class Player:
    def __init__(self, start_pos):
        self.row, self.col = start_pos


    def get_position(self):
        return self.row, self.col


    def move(self, direction, maze):
        direction_map = {
            'w': (-1, 0),
            's': (1, 0),
            'a': (0, -1),
            'd': (0, 1)
        }
        if direction in direction_map:
            r, c = direction_map[direction]
            new_row = self.row + r
            new_col = self.col + c
            if maze.is_walkable(new_row, new_col):
                self.row = new_row
                self.col = new_col
                return True
        return False


    def at_goal(self, goal_pos):
        """判断玩家是否到达终点"""
        return (self.row, self.col) == goal_pos