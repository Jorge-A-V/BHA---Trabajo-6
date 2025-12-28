from helpers.grid import grid
import numpy as np

class RTA:

    def __init__(self, grid: grid):
        self.grid = grid
        self.gn = 0
        self.traza = []
        self.nodo_final = None

    def run(self):
        nodo = self.grid.inicio

        while nodo:
            nodo = self.step(nodo)
            if self.grid.es_solucion(nodo):
                break
        
        self.nodo_final = nodo

    def step(self, id_nodo_actual):
        nodo_actual = self.grid.get(id_nodo_actual)
        vecinos = self.grid.vecinos(id_nodo_actual)

        print(vecinos)
        fns = [
            self.fn(self.grid.h(vecino_id)) for vecino_id in vecinos
        ]

        pos_vecino_min = np.argmin(fns)

        fn_min = fns[pos_vecino_min]
        vecino_id_min = vecinos[pos_vecino_min]

        self.grid.actualizar(id_nodo_actual, fn_min)
        self.gn += 1
        self.traza.append(id_nodo_actual)

        siguiente_nodo = vecino_id_min

        return siguiente_nodo

    def fn(self, vecino_h):
        c_vecino = 1 # Enunciado
        return c_vecino + vecino_h
