from .rta import RTA
import numpy as np

class LRTA(RTA):

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