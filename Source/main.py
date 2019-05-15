import time
import search
import P1
import P2

def main():
    water_jug_prob = P1.WaterJugProblem((0, 0), (2, 0), (4, 3))
    print(search.breadth_first_tree_search(water_jug_prob).solution())

    puzzle_prob = P2.NPuzzleProblem((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11, 13, 14, 15, 12), \
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0), 4)
    print(search.breadth_first_graph_search(puzzle_prob).solution())

if __name__ == "__main__":
    main()
