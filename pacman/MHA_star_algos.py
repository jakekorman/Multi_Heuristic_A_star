# ------------------------------- IMPORTS ------------------------------------#


import heapq
import util

# ------------------------------- CONSTANTS --------------------------------- #


INF = float('inf')
GOAL = "goal"
ANCHOR = 0
INAD = 1
PREV = 0
ACTION = 1
PATH_COST = 2
FIRST_IDX = 0
PACMAN_LOC = 0
FOOD = 1


# ------------------------------ FUNCTIONS -----------------------------------#


def remove_from_priority_queue(state, priority_queue):
    """
    Removes a specific element from the priority queue (item not at the back)
    """
    for i, elem in enumerate(priority_queue.heap):
        # check if element in priority queue is the element we want to remove
        if elem[2][PACMAN_LOC] == state[PACMAN_LOC] and elem[2][FOOD] == \
                state[FOOD]:
            priority_queue.heap[i] = priority_queue.heap[-1]
            break
    heapq.heapify(priority_queue.heap)


def path_generator(state, nodes_i):
    """
    Once we have reached a goal state which fits the criteria we recursively
    return the actions on the path to this node.
    """
    actions_list = [nodes_i[state][ACTION]]
    curr_state = state
    while nodes_i[curr_state][PREV]:  # while the state has
        # predecessor
        curr_state = nodes_i[curr_state][PREV]
        action = nodes_i[curr_state][ACTION]
        if action:
            actions_list.insert(FIRST_IDX, action)
    return actions_list


def key_value(problem, state, i, heuristics, w1, nodes):
    """
    value of state to be kept in the open list
    """
    if problem.is_goal_state(state):

        if nodes[GOAL][PATH_COST] > nodes[state][PATH_COST]:
            nodes[GOAL] = nodes[state]

    return nodes[state][PATH_COST] + w1 * heuristics[i](state, problem)


def independant_expand_state(problem, state, i, open_list, closed_list, w1,
                             heuristics, nodes):
    """
    Independent MHA* expand state function
    """
    for succ, action, step_cost in problem.get_successors(state):

        if succ not in nodes[i]:
            nodes[i][succ] = [None, None, INF]

        if nodes[i][succ][PATH_COST] > nodes[i][state][PATH_COST] + step_cost:
            nodes[i][succ] = [state, action, nodes[i][state][PATH_COST] + step_cost]

            if succ not in closed_list[i]:
                open_list[i].push(succ,key_value(problem, succ, i, heuristics, w1, nodes[i]))


def imha_star(problem, w1, w2, heuristics):
    """
    Independent MHA* function.
    Problem: pacman problem
    w1: First bound
    w2: Second bound
    Heuristics: List of n + 1 heuristics with heuristic 0 being consistent and
    the rest possibly being not admissible
    """
    start_state = problem.get_start_state()
    num_heuristics = len(heuristics)
    open_list = list()  # list of priority queues
    closed_list = list()  # list of sets (visited)
    nodes = list()  # list of dictionaries of {node:[prev, action, path_cost]}

    for i in range(num_heuristics):
        # to do maybe add to state so no dict
        nodes.append(dict())
        open_list.append(util.PriorityQueue())
        closed_list.append(set())
        nodes[i][start_state] = [None, None, 0]
        nodes[i][GOAL] = [None, None, INF]
        open_list[i].push(start_state, key_value(problem, start_state, i,heuristics, w1, nodes[i]))

    while open_list[0].min_key() < INF:
        for i in range(1, num_heuristics):
            if open_list[i].min_key() <= w2 * open_list[0].min_key():
                if nodes[i][GOAL][PATH_COST] <= open_list[i].min_key():
                    # path_cost of goal smaller than the minimum key
                    if nodes[i][GOAL][PATH_COST] < INF:
                        return path_generator(GOAL, nodes[i])

                else:
                    curr = open_list[i].pop()
                    independant_expand_state(problem, curr, i, open_list,
                                             closed_list, w1,heuristics, nodes)
                    closed_list[i].add(curr)

            else:
                if nodes[i][GOAL][PATH_COST] <= open_list[0].min_key():
                    if nodes[i][GOAL][PATH_COST] < INF:
                        return path_generator(GOAL, nodes[0])

                else:
                    curr = open_list[0].pop()
                    independant_expand_state(problem, curr, 0, open_list,
                                             closed_list, w1, heuristics,nodes)
                    closed_list[0].add(curr)


def shared_expand_state(problem, state, open_list, closed_list, w1, w2,
                        heuristics,
                        nodes):
    """
    Shared MHA* expand state function
    """
    for i in range(len(heuristics)):
        remove_from_priority_queue(state, open_list[i])

    for succ, action, step_cost in problem.get_successors(state):
        if succ not in nodes:
            nodes[succ] = [None, None, INF]

        if nodes[succ][PATH_COST] > nodes[state][PATH_COST] + step_cost:

            nodes[succ] = [state, action, nodes[state][PATH_COST] + step_cost]
            if succ not in closed_list[ANCHOR]:

                open_list[0].push(succ, key_value(problem, succ, 0,
                                                  heuristics, w1, nodes))
                if succ not in closed_list[INAD]:
                    for i in range(1, len(heuristics)):
                        key_s_i = key_value(problem, succ, i, heuristics, w1,
                                            nodes)
                        key_s_0 = key_value(problem, succ, 0, heuristics, w1,
                                            nodes)
                        if key_s_i <= w2 * key_s_0:
                            open_list[i].push(succ, key_s_i)


def smha_star(problem, w1, w2, heuristics):
    """
    Independant MHA* function
    Problem: pacman problem
    w1: First bound
    w2: Second bound
    Heuristics: List of n + 1 heuristics with heuristic 0 being consistent and
    the rest possibly being not admissable
    """
    start_state = problem.get_start_state()
    num_heuristics = len(heuristics)
    nodes = {GOAL: [None, None, INF], start_state: [None, None, 0]}
    open_list = list()  # list of priority queues
    for i in range(num_heuristics):
        open_list.append(util.PriorityQueue())
        open_list[i].push(start_state,
                          key_value(problem, start_state, i, heuristics, w1,
                                    nodes))
    closed_list = [set(), set()]  # Anchor and inad
    while open_list[0].min_key() < INF:

        for i in range(1, num_heuristics):
            if open_list[i].min_key() <= w2 * open_list[0].min_key():

                if nodes[GOAL][PATH_COST] <= open_list[i].min_key():
                    if nodes[GOAL][PATH_COST] < INF:
                        return path_generator(GOAL, nodes)

                else:
                    curr = open_list[i].pop()
                    shared_expand_state(problem, curr, open_list, closed_list,
                                        w1, w2, heuristics, nodes)
                    closed_list[INAD].add(curr)

            else:

                if nodes[GOAL][PATH_COST] <= open_list[0].min_key():
                    if nodes[GOAL][PATH_COST] < INF:
                        return path_generator(GOAL, nodes)

                else:
                    curr = open_list[0].pop()
                    shared_expand_state(problem, curr, open_list, closed_list,
                                        w1, w2, heuristics, nodes)
                    closed_list[ANCHOR].add(curr)
