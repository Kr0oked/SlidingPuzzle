__author__ = 'Philipp Bobek'
__copyright__ = 'Copyright (C) 2015 Philipp Bobek'
__license__ = 'Public Domain'
__version__ = '1.0'


import os


class Solver:

    SOLUTION_FOUND = 'Solution found'
    NO_SOLUTION = 'No solution'
    verbose = True
    file = None

    def __init__(self, is_verbose=True, output_file=None):
        self.verbose = is_verbose
        self.file = output_file

    def print_node(self, node):
        message = str(node)
        if self.verbose:
            print(message)
        if self.file is not None:
            self.file.write(message + os.linesep)

    def print_solution_found(self, node):
        message = self.SOLUTION_FOUND + os.linesep + str(node)
        print(message)
        if self.file is not None:
            self.file.write(message + os.linesep)

    def print_no_solution_found(self):
        message = self.NO_SOLUTION + os.linesep
        print(message)
        if self.file is not None:
            self.file.write(message + os.linesep)

    def breadth_first_search(self, node_list):
        new_nodes = []
        for node in node_list:
            self.print_node(node)
            if node.is_goal():
                self.print_solution_found(node)
                return self.SOLUTION_FOUND
            new_nodes.extend(node.get_successors())
        if len(new_nodes) != 0:
            return self.breadth_first_search(new_nodes)
        else:
            self.print_no_solution_found()
            return self.NO_SOLUTION

    def depth_first_search(self, node):
        self.print_node(node)
        if node.is_goal():
            self.print_solution_found(node)
            return self.SOLUTION_FOUND
        new_nodes = node.get_successors()
        while len(new_nodes) != 0:
            result = self.depth_first_search(new_nodes[0])
            if result == self.SOLUTION_FOUND:
                return self.SOLUTION_FOUND
            new_nodes = new_nodes[1:]
        return self.NO_SOLUTION

    def depth_first_search_b(self, node, depth, limit):
        self.print_node(node)
        if node.is_goal():
            self.print_solution_found(node)
            return self.SOLUTION_FOUND
        new_nodes = node.get_successors()
        while len(new_nodes) != 0 and depth < limit:
            result = self.depth_first_search_b(new_nodes[0], depth + 1, limit)
            if result == self.SOLUTION_FOUND:
                return self.SOLUTION_FOUND
            new_nodes = new_nodes[1:]
        return self.NO_SOLUTION

    def iterative_deepening(self, node):
        depth_limit = 0
        result = self.NO_SOLUTION
        while result is not self.SOLUTION_FOUND:
            result = self.depth_first_search_b(node, 0, depth_limit)
            depth_limit += 1
