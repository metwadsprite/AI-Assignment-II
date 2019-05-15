import time
import search
import P1
import P2

def main():
    # ----------------------------------- Water Jug Problem -------------------------------------- #

    water_jug_prob = P1.WaterJugProblem((0, 0), (2, 0), (4, 3))
    
    t0 = time.time()
    sol1 = search.breadth_first_tree_search(water_jug_prob).solution()
    
    t1 = time.time()
    sol2 = search.astar_search(water_jug_prob).solution()
    
    dt2 = time.time() - t1
    dt1 = t1 - t0

    print(sol1)
    print(sol2)
    
    print("Uninformed search time: {0:.4f} seconds\nInformed search time: {1:.4f} seconds".format(dt1, dt2))

    # -------------------------------------------------------------------------------------------- #

    # ----------------------------------- N-Puzzle Problem: -------------------------------------- #

    puzzle_prob = P2.NPuzzleProblem((5, 1, 2, 4, 7, 6, 3, 8, 9, 14, 10, 12, 13, 0, 11, 15), \
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0), 4)
    
    t0 = time.time()
    sol1 = search.astar_search(puzzle_prob, puzzle_prob.h1).solution()
    
    t1 = time.time()
    sol2 = search.astar_search(puzzle_prob, puzzle_prob.h2).solution()
    
    dt2 = time.time() - t1
    dt1 = t1 - t0
    
    print(sol1)
    print(sol2)
    
    print("Heuristic 1 search time: {0:.4f} seconds\nHeuristic 2 search time: {1:.4f} seconds".format(dt1, dt2))

    # -------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    main()
