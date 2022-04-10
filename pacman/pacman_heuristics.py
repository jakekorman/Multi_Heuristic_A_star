# ------------------------------- IMPORTS ------------------------------------#

import util

# ---------------------------- Consistent Heuristic    -----------------------#


def max_manhattan_distance(state, problem):
    """
    consistent pacman heuristic
    """
    position, food_grid = state
    remaining_food = food_grid.asList()
    if len(remaining_food) == 0:
        return 0
    distance_list = [util.manhattanDistance(position, food) for food in
                     remaining_food]
    return max(distance_list)

# --------------------------- Rest of The Heuristics--------------------------#


def max_two_food_distance(state, problem):
    """
    returns the maximum distance between any two food coordinates
    """
    max_dist = 0
    position, food_grid = state
    food_coords = food_grid.asList()
    for index, food in enumerate(food_coords):
        for i in range(index + 1, len(food_coords)):
            manhattan_dist_food = util.manhattanDistance(food, food_coords[i])
            if manhattan_dist_food > max_dist:
                max_dist = manhattan_dist_food
    return max_dist * 2


def amount_food_left(state, problem):
    """
    returns the amount of food multiplied by 2
    """
    position, food_grid = state
    return len(food_grid.asList()) * 2


def four_quarters(state, problem):
    """
    We divide the board into 4 quarters equally then check which of the 4
    corners has food remaining. returns (board width + board height) times
    the amount of corners with food remaining.
    """
    position, food_grid = state
    grid_h = food_grid.height
    grid_w = food_grid.width
    q_1 = q_2 = q_3 = q_4 = 0
    remaining_food = food_grid.asList()
    for food in remaining_food:

        if food[0] < grid_w/2 and food[1] > grid_h/2:
            q_1 = 1
            continue
        if food[0] >= grid_w/2 and food[1] > grid_h/2:
            q_2 = 1
            continue
        if food[0] < grid_w/2 and food[1] <= grid_h/2:
            q_3 = 1
            continue
        if food[0] >= grid_w/2 and food[1] <= grid_h/2:
            q_4 = 1
            continue
    return (q_1 + q_2 + q_3 + q_4) * (grid_w + grid_h) * 0.2