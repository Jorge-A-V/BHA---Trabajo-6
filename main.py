
from helpers.grid import grid
from algoritmos.rta import RTA

if __name__ == "__main__":
    grid_inicial = grid()

    print(grid_inicial.grid)

    algo = RTA(grid_inicial)

    algo.run()

    print(f"traza: {algo.traza}")