import re
import numpy as np

FILE_PATH = "./input.txt"
MAP_LENGTH = 101
MAP_HEIGHT = 103


class Robot:
    def __init__(self, initial_coords, velocity):
        self.initial_x = initial_coords[0]
        self.initial_y = initial_coords[1]
        self.velocity_x = velocity[0]
        self.velocity_y = velocity[1]

    def compute_tile_at_iteration(self, iteration, map_length=MAP_LENGTH, map_height=MAP_HEIGHT):
        return (
            (self.initial_x + iteration * self.velocity_x) % map_length,
            (self.initial_y + iteration * self.velocity_y) % map_height
        )


def read_input():
    robots = []
    with open(FILE_PATH, "r") as file:
        for robot in file:
            p_values = list(map(int, re.findall(r"p=([\d,-]+)", robot)[0].split(',')))
            v_values = list(map(int, re.findall(r"v=([\d,-]+)", robot)[0].split(',')))
            robots.append(Robot(p_values, v_values))

    return robots


def get_map_at_iteration(robots, iteration, map_length=MAP_LENGTH, map_height=MAP_HEIGHT):
    map_at_iteration = np.zeros((map_height, map_length))

    for robot in robots:
        x, y = robot.compute_tile_at_iteration(iteration, map_length, map_height)
        map_at_iteration[y, x] += 1

    return map_at_iteration


def save_map(iteration_map, iteration=None):
    file_title = "./output_" + str(iteration) + ".txt" if iteration is not None else "./output.txt"
    with open(file_title, "w") as output_file:
        for y in range(len(iteration_map)):
            line = ""
            for x in range(len(iteration_map[0])):
                if iteration_map[y][x] != 0:
                    line += "#"
                else:
                    line += " "
            print(line, file=output_file)


if __name__ == '__main__':
    robot_list = read_input()
    robots_map = get_map_at_iteration(robot_list, 100)
    save_map(robots_map)
