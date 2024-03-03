from algorithms.breadth_search import breadth_search
from algorithms.depth_search import depth_search
from basic.path import node_path, edge_path

from problems.puzzle_4 import Puzzle4


def test_puzzle_4_using_breadth_search():
    problem = Puzzle4()

    (visited_states_amount, solution_node) = breadth_search(problem)

    if (solution_node is None):
        print("There is no solution for the problem")
    else:
        path = edge_path(solution_node)
        print(f"Solution: {path}")
        

    print(f"Visited states: {visited_states_amount}")
    print("Initial state: ")
    print(problem.show(problem.root_node))


if __name__ == "__main__":
    test_puzzle_4_using_breadth_search()


