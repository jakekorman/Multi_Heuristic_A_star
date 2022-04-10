from ast import literal_eval

GIVENS = "Givens"
DATA = "Data"


class Parser:

    def __init__(self, input_file: str):
        file2parse = open(input_file, "r")
        self.input_lines = file2parse.read().splitlines()
        self.input_lines = list(
            filter(lambda line: line != "", self.input_lines))  # accounts for accidental empty lines
        self.idx = 0
        self.curr_line = self.input_lines[self.idx]
        self.curr_algo = None
        self.curr_board_size = None
        self.curr_weight_combo = None
        self.curr_runtime = None
        self.curr_cost = None
        self.curr_expanded = None
        file2parse.close()
        self.update_givens()

    def advance(self):
        if self.has_more_commands():
            self.idx += 1
            self.curr_line = self.input_lines[self.idx]
            self.update_givens()
            self.update_data()

    def update_data(self):
        if self.command_type() == DATA:
            parts = self.curr_line.split(",")
            self.curr_runtime = parts[0]
            self.curr_cost = parts[1]
            self.curr_expanded = parts[2]

    def update_givens(self):
        if self.command_type() == GIVENS:

            # extract board size tuple
            idx1 = self.curr_line.find("(")
            idx2 = self.curr_line.find(")")
            board_size_tuple = self.curr_line[idx1:idx2 + 2]
            self.curr_board_size = board_size_tuple

            # split up rest of line
            self.curr_line = self.curr_line[:idx1] + self.curr_line[idx2 + 2:]
            parts = self.curr_line.split(",")
            self.curr_algo = parts[0]

            # reset these values
            self.curr_runtime = None
            self.curr_cost = None
            self.curr_expanded = None

            if self.curr_algo != "Astar":
                self.curr_weight_combo = (parts[1], parts[2])

    def command_type(self):
        if self.curr_line[0].isupper():
            return GIVENS
        elif self.curr_line[0].isdigit():
            return DATA

    def has_more_commands(self):
        return self.idx < len(self.input_lines) - 1

    # Getters for givens
    def get_algo(self):
        return self.curr_algo

    def get_weight_combo(self):
        if self.curr_algo != "Astar":
            idx1 = self.curr_weight_combo[0].find("=")
            idx2 = self.curr_weight_combo[1].find("=")
            return (float(self.curr_weight_combo[0][idx1 + 1:]), float(self.curr_weight_combo[1][idx2 + 1:]))

    def get_board_size(self):
        if self.curr_algo != "Astar":
            str_tup = self.curr_board_size[:-1]
        else:
            str_tup = self.curr_board_size
        return literal_eval(str_tup)

    # Getters for data
    def get_runtime(self):
        return float(self.curr_runtime)

    def get_solution_cost(self):
        return int(self.curr_cost)

    def get_expanded_nodes(self):
        return int(self.curr_expanded)


class DataOrganizer:

    def __init__(self, algo):
        self.data = dict()
        self.algo = algo
        self.min_cost = None
        self.max_cost = None
        self.min_time = None
        self.max_time = None
        self.min_exp = None  # min amnt of expanded nodes
        self.max_exp = None  # max

    def insert_entry(self, weight_tuple, board_size, avgtup):
        if self.algo != "Astar":
            self.data[(weight_tuple, board_size)] = avgtup
        else:
            self.data[board_size] = avgtup
        self.update_mins_and_maxes(avgtup[0], avgtup[1], avgtup[2])

    def update_mins_and_maxes(self, runtime, cost, expanded):
        self.min_cost = cost if self.min_cost == None else min(self.min_cost, cost)
        self.max_cost = cost if self.max_cost == None else max(self.max_cost, cost)
        self.min_time = runtime if self.min_time == None else min(self.min_time, runtime)
        self.max_time = runtime if self.max_time == None else max(self.max_time, runtime)
        self.min_exp = expanded if self.min_exp == None else min(self.min_exp, expanded)
        self.max_exp = expanded if self.max_exp == None else max(self.max_exp, expanded)

    def get_data(self):
        return self.data

    def get_value(self, key):
        return self.data[key]

    def get_algo(self):
        return self.algo

    def get_min_cost(self):
        return self.min_cost

    def get_max_cost(self):
        return self.max_cost

    def get_min_time(self):
        return self.min_time

    def get_max_time(self):
        return self.max_time

    def get_min_exp(self):
        return self.min_exp

    def get_max_exp(self):
        return self.max_exp


def calculate_averages(parser: Parser):
    sum_runtimes = 0
    sum_costs = 0
    sum_expanded = 0
    for i in range(3):  # three iterations, one for each board type
        parser.advance()
        sum_runtimes += parser.get_runtime()
        sum_costs += parser.get_solution_cost()
        sum_expanded += parser.get_expanded_nodes()

    return sum_runtimes / 3, sum_costs / 3, sum_expanded / 3


def set_up_Data_organizer(parser: Parser):
    new_DO = DataOrganizer(parser.get_algo())
    while parser.has_more_commands():
        avgs = calculate_averages(parser)
        new_DO.insert_entry(parser.get_weight_combo(), parser.get_board_size(), avgs)
        parser.advance()
    return new_DO


def initialize_DOs():
    Astar_parser = Parser("Final_Data/Astar_results.txt")
    WAstar_parser = Parser("Final_Data/WAstar_results.txt")
    IMHAstar_parser = Parser("Final_Data/IMHAstar_results.txt")
    SMHAstar_parser = Parser("Final_Data/SMHAstar_results.txt")

    Astar_DO = set_up_Data_organizer(Astar_parser)
    WAstar_DO = set_up_Data_organizer(WAstar_parser)
    IMHAstar_DO = set_up_Data_organizer(IMHAstar_parser)
    SMHAstar_DO = set_up_Data_organizer(SMHAstar_parser)

    return [Astar_DO, WAstar_DO, IMHAstar_DO, SMHAstar_DO]
