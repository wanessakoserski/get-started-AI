import random 
import numpy as np
from basic.node import Node

class Puzzle4:
    def __init__(self):
        self.goal_state = np.array(["1", "2", "3", "_"])
        self.initial_state = np.array(["_", "1", "2", "3"])
        np.random.shuffle(self.initial_state)

    def start(self):
        self.root_node = Node(self.initial_state)
        return self.root_node
    
    def show(self, node):
        state = node.state
        
        final_state = ""
        for i in range(4):
            final_state += " | " + state[i]
            if (i == 1):
                final_state += "\n"
        
        return final_state

    def test_goal(self, node):
        return np.array_equal(node.state, self.goal_state)
    
    def generate_next_nodes(self, node):
        state = node.state
        next_nodes = []

        position = np.where(state == "_")[0][0]

        possibilities = []
        if node.edge == "⬅":
            possibilities = [self._left, self._up, self._down]
        elif node.edge == "⬆":
            possibilities = [self._right, self._left, self._up]
        elif node.edge == "⬇":
            possibilities = [self._right, self._left, self._down]
        elif node.edge == "➡":
            possibilities = [self._right, self._up, self._down]
        else:
            possibilities = [self._right, self._left, self._up, self._down]

        random.shuffle(possibilities)

        for possibility in possibilities:
            next_node = possibility(position, node)
            if next_node is not None:
                next_nodes.append(next_node)

        return next_nodes

    def _up(self, position, node):
        if position not in [0, 1]:
            next_state = np.copy(node.state)
            next_state[position] = next_state[position - 2]
            next_state[position - 2] = "_"
            return Node(next_state, node, "⬆")
        else:
            return None
        
    def _down(self, position, node):
        if position not in [2, 3]:
            next_state = np.copy(node.state)
            next_state[position] = next_state[position + 2]
            next_state[position + 2] = "_"
            return Node(next_state, node, "⬇")
        else:
            return None
        
    def _left(self, position, node):
        if position not in [0, 2]:
            next_state = np.copy(node.state)
            next_state[position] = next_state [position - 1]
            next_state[position - 1] = "_"
            return Node(next_state, node, "⬅")
        else:
            return None
        
    def _right(self, position, node):
        if position not in [1, 3]:
            next_state = np.copy(node.state)
            next_state[position] = next_state[position + 1]
            next_state[position + 1] = "_"
            return Node(next_state, node, "➡")
        else:
            return None