import time
from eight_puzzle import *
from search import *

def main():
    
    problem_miss = EightPuzzleMiss((1, 2, 3, 4, 8, 0, 7, 6, 5), (1, 2, 3, 4, 5, 6, 7, 8, 0))
    problem_mht = EightPuzzleMht((1, 2, 3, 4, 8, 0, 7, 6, 5), (1, 2, 3, 4, 5, 6, 7, 8, 0))

    t1 = time.time()
    path = astar_search(problem_miss).solution()
    t2 = time.time()
    t3 = time.time()
    path2 = astar_search(problem_mht).solution()
    t4 = time.time()
    print(path, '\n', t2 - t1)
    print(path2, '\n', t4 - t3)

    """ Compare searchers """
    compare_searchers(problems=[problem_miss, problem_mht],
                      header=['Searcher', 'A* h1(n)',
                              'A* h2(n)'], searchers=[
            astar_search,
            recursive_best_first_search])


if __name__ == "__main__":
    main()
