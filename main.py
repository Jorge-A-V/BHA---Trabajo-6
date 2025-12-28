
from helpers.grid import grid

if __name__ == "__main__":
    grid_inicial = grid()

    print(grid_inicial.grid)

    grid_inicial.cambiar_inicio(2)

    print(grid_inicial.grid)