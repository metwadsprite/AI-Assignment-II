import time
import search
import P1

def main():
    water_jug_prob = P1.WaterJugProblem((0, 0), (2, 0), (4, 3))
    print(search.breadth_first_tree_search(water_jug_prob))

if __name__ == "__main__":
    main()
