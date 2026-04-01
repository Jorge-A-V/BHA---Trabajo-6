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

        # mantener monotonia
        nueva_h = max(fn_min, self.grid.h(id_nodo_actual))

        self.grid.actualizar(id_nodo_actual, nueva_h)
        
        self.traza.append(id_nodo_actual)

        siguiente_nodo = vecino_id_min

        self.actualizar_historial(
            gn_actual = self.gn, nodo_actual = id_nodo_actual,
            h_nuevo = fn_min, siguiente_nodo = siguiente_nodo, 
            f_siguiente = fns[pos_vecino_min]
        )

        self.gn += 1

        return siguiente_nodo