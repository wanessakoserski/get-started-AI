import random 
import numpy as np 
from basic.node import Node

class Trail:
    def __init__(self):
        self.goal_state = np.array([" A ", " T ", " T ", " # ", " T ", " T ", " T ", " - ",
                                    " T ", " A ", " T ", " T ", " T ", " M ", " # ", " T ",
                                    " # ", " T ", " A ", " # ", " T ", " M ", " # ", " # ",
                                    " T ", " # ", " T ", " A ", " T ", " A ", " A ", " A ",
                                    " T ", " T ", " T ", " T ", " A ", " T ", " T ", " T ",
                                    " T ", " M ", " # ", " T ", " A ", " # ", " T ", " T ",
                                    " T ", " M ", " T ", " T ", " T ", " A ", " # ", " T ",
                                    " T ", " T ", " T ", " T ", " # ", " T ", " A ", " T "])
        self.initial_state = np.array([" A ", " T ", " T ", " # ", " T ", " T ", " T ", " T ",
                                       " T ", " A ", " T ", " T ", " T ", " M ", " # ", " T ",
                                       " # ", " T ", " A ", " # ", " T ", " M ", " # ", " # ",
                                       " T ", " # ", " T ", " A ", " T ", " A ", " A ", " A ",
                                       " T ", " T ", " T ", " T ", " A ", " T ", " T ", " T ",
                                       " T ", " M ", " # ", " T ", " A ", " # ", " T ", " T ",
                                       " T ", " M ", " T ", " T ", " T ", " A ", " # ", " T ",
                                       " - ", " T ", " T ", " T ", " # ", " T ", " A ", " T "])
        self.top = [0, 1, 2, 3, 4, 5, 6, 7]
        self.bottom = [56, 57, 58, 59, 60, 61, 62, 63]
        self.right = [7, 15, 23, 31, 39, 47, 55, 63]
        self.left = [0, 8, 16, 24, 32, 40, 48, 56]

    def start(self):
        self.root_node = Node(self.initial_state)
        return self.root_node
    
    def show(self, node):
        state = node.state

        final_state = ""
        for i in range(8):
            for j in range(8):
                final_state += state[(i * 8) + j]
            final_state += "\n"

        return final_state
    
    def test_goal(self, node):
        return node.state[7] == " - "
    
    def generate_next_nodes(self, node):
        state = node.state
        next_nodes = []

        position = np.where(state == " - ")[0]

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
        if position not in self.top and node.state[position - 8] != " # ":
            next_state = np.copy(node.state)
            next_state[position] = next_state[position - 8]
            next_state[position - 8] = " - "
            return Node(next_state, node, "⬆")
        else:
            return None
        
    def _down(self, position, node):
        if position not in self.bottom and node.state[position + 8] != " # ":
            next_state = np.copy(node.state)
            next_state[position] = next_state[position + 8]
            next_state[position + 8] = " - "
            return Node(next_state, node, "⬇")
        else:
            return None
        
    def _left(self, position, node):
        if position not in self.left and node.state[position - 1] != " # ":
            next_state = np.copy(node.state)
            next_state[position] = next_state [position - 1]
            next_state[position - 1] = " - "
            return Node(next_state, node, "⬅")
        else:
            return None
        
    def _right(self, position, node):
        if position not in self.right and node.state[position + 1] != " # ":
            next_state = np.copy(node.state)
            next_state[position] = next_state[position + 1]
            next_state[position + 1] = " - "
            return Node(next_state, node, "➡")
        else:
            return None
        
    def heuristic(self, node):
        state = node.state
        result = self.goal_state
        return sum(1 for i in range(len(result)) if result[i] == state[i])
    
    def cost(self, node, destination_node):
        # finding position where the point move to calculate the cost to be in that position 
        position = np.where(destination_node.state == " - ")[0]
        value = node.state[position]

        if (value == " T "):
            return 1
        elif (value == " A "):
            return 3
        elif (value == " M "):
            return 6
        else:
            return 0