import random
import numpy as np
from basic.node import Node

class Maze:
    def __init__(self):
        self.goal_state = np.array([" . ", " # ", " . ", " . ", " . ",
                                    " . ", " . ", " # ", " . ", " . ",
                                    " . ", " # ", " . ", " # ", " . ",
                                    " . ", " . ", " . ", " . ", " # ",
                                    " # ", " # ", " # ", " H ", " . "])
        self.initial_state = np.array(([" H ", " # ", " . ", " . ", " . ",
                                        " . ", " . ", " # ", " . ", " . ",
                                        " . ", " # ", " . ", " # ", " . ",
                                        " . ", " . ", " . ", " . ", " # ",
                                        " # ", " # ", " # ", " . ", " . "]))
        
    def start(self):
        self.root_node = Node(self.initial_state)
        return self.root_node
    
    def show(self, node):
        state = node.state

        final_state = ""
        for i in range(25):
            if (i % 5 == 0):
                final_state += "\n"
            final_state += state[i]
            
        return final_state
    
    def test_goal(self, node):
        return np.array_equal(node.state, self.goal_state)
    
    def generate_next_nodes(self, node):
        state = node.state
        next_nodes = []

        position = np.where(state == " H ")[0][0]

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
        if position not in [0, 1, 2, 3, 4] and node.state[position - 5] != " # ":
            next_state = np.copy(node.state)
            next_state[position] = next_state[position - 5]
            next_state[position - 5] = " H "
            return Node(next_state, node, "⬆")
        else:
            return None
        
    def _down(self, position, node):
        if position not in [20, 21, 22, 23, 24] and node.state[position + 5] != " # ":
            next_state = np.copy(node.state)
            next_state[position] = next_state[position + 5]
            next_state[position + 5] = " H "
            return Node(next_state, node, "⬇")
        else:
            return None
        
    def _left(self, position, node):
        if position not in [0, 5, 10, 15, 20] and node.state[position - 1] != " # ":
            next_state = np.copy(node.state)
            next_state[position] = next_state [position - 1]
            next_state[position - 1] = " H "
            return Node(next_state, node, "⬅")
        else:
            return None
        
    def _right(self, position, node):
        if position not in [4, 9, 14, 19, 24] and node.state[position + 1] != " # ":
            next_state = np.copy(node.state)
            next_state[position] = next_state[position + 1]
            next_state[position + 1] = " H "
            return Node(next_state, node, "➡")
        else:
            return None