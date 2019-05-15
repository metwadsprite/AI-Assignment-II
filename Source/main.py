import time
import search
import P1
import P2

def main():
    water_jug_prob = P1.WaterJugProblem((0, 0), (2, 0), (4, 3))
    print(search.breadth_first_tree_search(water_jug_prob).solution())

    puzzle_prob = P2.NPuzzleProblem((3, 4, 14, 13, 6, 2, 1, 0, 11, 8, 5, 10, 12, 15, 7, 9), \
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0), 4)
    # print(search.breadth_first_graph_search(puzzle_prob).solution())

    print(search.astar_search(puzzle_prob).solution())

if __name__ == "__main__":
    main()
