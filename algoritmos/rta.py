from helpers.grid import grid
import numpy as np

class RTA:

    def __init__(self, grid: grid, imprimir_traza = True):
        self.grid = grid
        self.gn = 0
        self.traza = []
        self.nodo_final = None
        self.historial_para_imprimir = []

    def run(self):
        nodo = self.grid.inicio

        if self.grid.es_solucion(nodo):
            # ya estamos (edge case)
            self.nodo_final = nodo
            return

        while nodo:
            nodo = self.step(nodo)
            if self.grid.es_solucion(nodo):
                break
        
        self.nodo_final = nodo

    def actualizar_historial(self, gn_actual, nodo_actual, h_nuevo, siguiente_nodo, f_siguiente):
        self.historial_para_imprimir.append(
            {
                "gn": gn_actual,
                "nodo_actual": nodo_actual,
                "h_nueva": h_nuevo,
                "siguiente_nodo": siguiente_nodo,
                "f_siguiente": f_siguiente
            }
        )

    def step(self, id_nodo_actual):
        nodo_actual = self.grid.get(id_nodo_actual)
        vecinos = self.grid.vecinos(id_nodo_actual)

        fns = [
            self.fn(self.grid.h(vecino_id)) for vecino_id in vecinos
        ]

        pos_vecino_min = np.argmin(fns)
        pos_vecino_segundo_min = self.segundo_min(fns)

        fn_segundo_min = fns[pos_vecino_segundo_min]
        vecino_id_min = vecinos[pos_vecino_min]

        self.grid.actualizar(id_nodo_actual, fn_segundo_min)
        
        self.traza.append(id_nodo_actual)

        siguiente_nodo = vecino_id_min

        self.actualizar_historial(
            gn_actual = self.gn, nodo_actual = id_nodo_actual,
            h_nuevo = fn_segundo_min, siguiente_nodo = siguiente_nodo, 
            f_siguiente = fns[pos_vecino_min]
        )

        self.gn += 1

        return siguiente_nodo

    def fn(self, vecino_h):
        c_vecino = 1 # Enunciado
        return c_vecino + vecino_h

    def segundo_min(self, array):
        if len(array) == 1:
            # no vecinos, se devuelve a si mismo
            # es decir, convencion para usar el fn disponible
            return 0

        pos_minimo = np.argmin(array)

        # mascara con infinito
        temp = np.array(array, dtype=float)
        temp[pos_minimo] = np.inf

        pos_segundo_minimo = np.argmin(temp)
        return pos_segundo_minimo

    def imprimir_historial(self):
        print("\n" + "="*70)
        print(f"{'PASO':<6} | {'NODO ACTUAL':<12} | {'H NUEVO':<8} | {'SIG.NODO':<12} | {'F SIG.':<6}")
        print("-"*70)
        for h in self.historial_para_imprimir:
            print(f"{h['gn']:<3}    | {str(h['nodo_actual']):<12} | {h['h_nueva']:<8.2f} | {str(h['siguiente_nodo']):<12} | {h['f_siguiente']:.2f}")
        print("="*70 + "\n")

    def imprimir_historial_latex(self):
        """Para copiar mas facil al informe"""
        print("\\begin{table}[h!]")
        print("\\centering")
        print("\\begin{tabular}{|c|c|c|c|c|}")
        print("\\hline")
        print("\\textbf{Paso} & \\textbf{Nodo Actual} & \\textbf{H Nuevo} & \\textbf{Sig. Nodo} & \\textbf{F Sig.} \\\\ \\hline")
        for h in self.historial_para_imprimir:
            print(f"{h['gn']} & {h['nodo_actual']} & {h['h_nueva']:.2f} & {h['siguiente_nodo']} & {h['f_siguiente']:.2f} \\\\ \\hline")
        print("\\end{tabular}")
        print("\\caption{Traza de ejecución del algoritmo RTA*}")
        print("\\label{tab:traza_rta}")
        print("\\end{table}")
