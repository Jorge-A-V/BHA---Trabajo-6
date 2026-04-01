
from helpers.grid import grid, posiciones_iniciales_extra
from algoritmos.rta import RTA
from algoritmos.lrta import LRTA

if __name__ == "__main__":
    grid_rta = grid()
    
    print(grid_rta.grid)

    rta = RTA(grid_rta)
    rta.run()

    rta.imprimir_historial()


def fuera():
    for idx, posicion_inicial_extra in enumerate(posiciones_iniciales_extra):
        grid_rta.cambiar_inicio_sin_cargar_dist(idx)
        rta = RTA(grid_rta)
        rta.run()

    grid_lrta = grid()
    lrta = LRTA(grid_lrta)
    lrta.run()

    for idx, posicion_inicial_extra in enumerate(posiciones_iniciales_extra):
        grid_lrta.cambiar_inicio_sin_cargar_dist(idx)
        lrta = LRTA(grid_lrta)
        lrta.run()

