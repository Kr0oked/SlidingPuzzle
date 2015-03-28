__author__ = 'Philipp Bobek'
__copyright__ = 'Copyright (C) 2015 Philipp Bobek'
__license__ = 'Public Domain'
__version__ = '1.0'


import os
import copy
from random import randint


class Board:

    blocks = 0
    size = 0

    def __init__(self, blocks_on_start):
        self.blocks = blocks_on_start
        self.size = len(self.blocks)

    def __str__(self):
        output = ''
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.blocks[x][y] != self.size * self.size - 1:
                    output += str(self.blocks[x][y] + 1)
                output += '\t'
            output += os.linesep
        return output

    def is_goal(self):
        previous = -1
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.blocks[x][y] > previous:
                    previous = self.blocks[x][y]
                else:
                    return False
        return True

    def get_successors(self):
        neighbors = []
        blank_block_coordinates = self.get_blank_block()
        x = blank_block_coordinates[0]
        y = blank_block_coordinates[1]

        if x != 0:
            neighbors.append(Board(self.swap_blocks(copy.deepcopy(self.blocks), x, y, x-1, y)))
        if y != 0:
            neighbors.append(Board(self.swap_blocks(copy.deepcopy(self.blocks), x, y, x, y-1)))
        if x != self.size-1:
            neighbors.append(Board(self.swap_blocks(copy.deepcopy(self.blocks), x, y, x+1, y)))
        if y != self.size-1:
            neighbors.append(Board(self.swap_blocks(copy.deepcopy(self.blocks), x, y, x, y+1)))

        return neighbors

    def get_blank_block(self):
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.blocks[x][y] == self.size * self.size - 1:
                    return x, y

    @staticmethod
    def swap_blocks(blocks_for_swapping, x1, y1, x2, y2):
        tmp = blocks_for_swapping[x1][y1]
        blocks_for_swapping[x1][y1] = blocks_for_swapping[x2][y2]
        blocks_for_swapping[x2][y2] = tmp
        return blocks_for_swapping

    @staticmethod
    def make_random_board(random_moves):
        blocks_start = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        board = Board(blocks_start)
        for x in range(0, random_moves):
            successors = board.get_successors()
            size = len(successors)
            board = successors[randint(0, size-1)]
        return board
