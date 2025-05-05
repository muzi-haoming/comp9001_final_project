from maze import Maze
from player import Player

def play_maze(level_path_list):
    for i, level_path in enumerate(level_path_list):
        print("Welcome to the maze game!")
        print("The first pass:")

        maze = Maze(level_path)
        player = Player(maze.start)

        print("🎮 The maze game begins! Input w/a/s/d to move up/left/down/right")
        print("🔚 Reach E to end the game!")

        while True:
            maze.print_maze(player.get_position())
            move = input("你的移动 (w/a/s/d): ").lower()

            if move not in ['w', 'a', 's', 'd']:
                print("⚠️ 无效输入，请输入 w/a/s/d。")
                continue

            if not player.move(move, maze):
                print("🚧 撞墙啦，不能走这边！")

            if player.at_goal(maze.end):
                maze.print_maze(player.get_position())
                print("🎉 恭喜你到达终点！游戏结束。")
                break

if __name__ == "__main__":
    level_file_list = ["levels/level_1.txt", "levels/level_2.txt", "levels/level_3.txt"]
    play_maze(level_file_list)
