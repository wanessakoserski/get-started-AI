from basic.path import node_path, edge_path

from algorithms.breadth_search import breadth_search
from algorithms.depth_search import depth_search
from algorithms.dijkstra import dijkstra
from algorithms.a_star import a_star

from problems.puzzle_4 import Puzzle4
from problems.puzzle_8 import Puzzle8
from problems.maze import Maze


def test_problem(problem, algorithm):
    (visited_states_amount, solution_node) = algorithm(problem)

    if (solution_node is None):
        print("There is no solution for the problem")
    else:
        path = edge_path(solution_node)
        print(f"Solution: {path}")

    print(f"Visited states: {visited_states_amount}")
    print("Initial state: ")
    print(problem.show(problem.root_node))


if __name__ == "__main__":
    problem = Puzzle4()

    print("\n\n>> Puzzle 4 with Breadth-First Search <<\n")
    test_problem(problem, breadth_search)

    print("\n\n>> Puzzle 4 with Depth-First Search <<\n")
    test_problem(problem, depth_search)


    problem = Maze()

    print("\n\n>> Maze with Breadth-First Search <<\n")
    test_problem(problem, breadth_search)

    print("\n\n>> Maze with Depth-First Search <<\n")
    test_problem(problem, depth_search)


    problem = Puzzle8()

    print("\n\n>> Puzzle 8 with Breadth-First Search <<\n")
    test_problem(problem, breadth_search)

    print("\n\n>> Puzzle 8 with Heuristic (with distance manhattan) <<\n")
    test_problem(problem, a_star)
