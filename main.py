
from helpers.grid import grid, posiciones_iniciales_extra
from algoritmos.rta import RTA
from algoritmos.lrta import LRTA


if __name__ == "__main__":
    grid_rta = grid()
    
    print("GRID ORIGINAL CON DISTANCIAS \n")
    grid_rta.imprimir_grid_h()

    rta = RTA(grid_rta)
    rta.run()

    rta.imprimir_historial()
    rta.imprimir_historial_latex()
    rta.imprimir_traza()

    grid_rta.imprimir_grid_h()

    grid_rta.imprimir_grid_camino(rta.traza)

    for idx, posicion_inicial_extra in enumerate(posiciones_iniciales_extra):
        grid_rta.cambiar_inicio_sin_cargar_dist(idx)
        rta = RTA(grid_rta)
        rta.run()
        print(f"\nEJECUCCIÓN {idx}\n")
        grid_rta.imprimir_grid_camino(rta.traza)

    grid_rta.imprimir_grid_h()

    grid_lrta = grid()
    lrta = LRTA(grid_lrta)
    lrta.run()

    lrta.imprimir_historial()
    lrta.imprimir_historial_latex()
    lrta.imprimir_traza()

    grid_lrta.imprimir_grid_h()

    grid_lrta.imprimir_grid_camino(lrta.traza)    

    for idx, posicion_inicial_extra in enumerate(posiciones_iniciales_extra):
        grid_lrta.cambiar_inicio_sin_cargar_dist(idx)
        lrta = LRTA(grid_lrta)
        lrta.run()
        print(f"\nEJECUCCIÓN {idx}\n")
        grid_lrta.imprimir_grid_camino(lrta.traza)

    grid_lrta.imprimir_grid_h()

