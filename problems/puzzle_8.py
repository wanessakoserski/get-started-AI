import random 
import numpy as np 
from basic.node import Node

class Puzzle8:
    def __init__(self):
        self.goal_state = np.array(["1", "2", "3", "4", "5", "6", "7", "8", "_"])
        self.initial_state = np.array(["_", "1", "2", "3", "4", "5", "6", "7", "8"])
        np.random.shuffle(self.initial_state)

    def start(self):
        self.root_node = Node(self.initial_state)
        return self.root_node
    
    def show(self, node):
        state = node.state

        final_state = ""
        for i in range(9):
            if (i % 3 == 0):
                final_state += "\n"
            final_state += " | " + state[i] 

        return final_state
    
    def test_goal(self, node):
        return np.array_equal(node.state, self.goal_state)
    
    def generate_next_nodes(self, node):
        state = node.state
        next_nodes = []

        position = np.where(state == "_")[0][0]

        possibilities = [self._right, self._left, self._up, self._down]
        random.shuffle(possibilities)
        for possibility in possibilities:
            next_node = possibility(position, node)
            if next_node is not None:
                next_nodes.append(next_node)

        return next_nodes

    def _up(self, position, node):
        if position not in [0, 1, 2]:
            next_state = np.copy(node.state)
            next_state[position] = next_state[position - 3]
            next_state[position - 3] = "_"
            return Node(next_state, node, "⬆")
        else:
            return None
        
    def _down(self, position, node):
        if position not in [6, 7, 8]:
            next_state = np.copy(node.state)
            next_state[position] = next_state[position + 3]
            next_state[position + 3] = "_"
            return Node(next_state, node, "⬇")
        else:
            return None
        
    def _left(self, position, node):
        if position not in [0, 3, 6]:
            next_state = np.copy(node.state)
            next_state[position] = next_state [position - 1]
            next_state[position - 1] = "_"
            return Node(next_state, node, "⬅")
        else:
            return None
        
    def _right(self, position, node):
        if position not in [2, 5, 8]:
            next_state = np.copy(node.state)
            next_state[position] = next_state[position + 1]
            next_state[position + 1] = "_"
            return Node(next_state, node, "➡")
        else:
            return None
        
    # Heuristic 1: Check whether the values are in correct place (sum matches)
    # it may difficult the arrival of a final result
    def heuristic_raw(self, node):
        state = node.state
        result = self.goal_state
        return sum(1 for i in range(len(result)) if result[i] == state[i])

    # Heuristic 2: distance to expected result
    # admissible heuristic, as the result always comes closer
    def heuristic(self, node):
        state = node.state
        result = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "_"]]
        matrix_state = [state[0:3], state[3:6], state[6:9]]

        sum = 0
        for i in range(len(result)):
            for j in range(len(result[i])):
                value = result[i][j]
                sum = sum + self._distance_manhattan(value, matrix_state, i, j)

        return sum

    # d = |xi-xj| + |yi-yj|
    def _distance_manhattan(self, value, state, i, j):
        for k in range(len(state)):
            for h in range(len(state[k])):
                if value == state[k][h]:
                    return abs(i - k) + abs(j - h)

    def cost(self, node, destination_node):
        return 1