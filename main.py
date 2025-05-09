from maze import Maze
from player import Player


def play_maze(level_path_list):
    print(">>>Welcome to the maze game!<<<")
    print("🎮 The maze game begins! Input w/a/s/d to move up/left/down/right or r/q to restart/quit")
    print("🔚 Reach E to end the game!")

    for i, level_path in enumerate(level_path_list):
        print(f">>Level {i + 1}<<")

        maze = Maze(level_path)
        player = Player(maze.start)

        while True:
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            maze.print_maze(player.get_position())
            move = input("Your input (w/a/s/d/r/q): ")

            if move not in ["w", "a", "s", "d", "r", "q"]:
                print("⚠️⚠️⚠️ Invalid input...")
                continue

            if move == "r":
                maze = Maze(level_path)
                player = Player(maze.start)
                print("The Map have been refreshed")
                continue

            if move == "q":
                i = -1
                break

            if not player.move(move, maze):
                print("🚧🚧🚧 You cannot move to here.")

            if player.at_goal(maze.end):
                maze.print_maze(player.get_position())
                print("🎉🎉🎉 Congratulations!")
                break

        if i == len(level_path_list) - 1:
            print(">>>🎉🎉🎉🎉🎉🎉 You have cleared all levels!🎉🎉🎉🎉🎉🎉<<<")

        if i == -1:
            print(">>>Bye~<<<")
            break


if __name__ == "__main__":
    level_file_list = ["levels/level_1.txt", "levels/level_2.txt", "levels/level_3.txt"]
    play_maze(level_file_list)
