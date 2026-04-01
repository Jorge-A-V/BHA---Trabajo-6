from .heuristicos import distancia_manhattan

PARED = "w"
AVATAR = "A"
SOLUCION = "X"
CAMINO = "C"

posiciones_iniciales_extra = ['2F', '1I', '5H', '5L', '1K', '4B', '3H', '3I', '5C', '5B']

letras = "ABCDEFGHIJKLM"
mapa_letras = {letra: idx for idx, letra in enumerate(letras)}
numeros = numeros = ['0','1','2','3','4','5','6']

class grid:

    grid_texto = """
  ABCDEFGHIJKLM
0 wwwwwwwwwwwww
1 w   w       w
2 www w w www w
3 w wAw w   w w
4 w w wwwww w w
5 w        Xw w
6 wwwwwwwwwwwww"""

    def __init__(self):

        self.grid = {}
        self.inicio_default = None
        self.inicio = None
        self.objetivo = None

        rows = self.grid_texto.split("\n")

        for i, (row, num) in enumerate(zip(rows[2:], numeros)):  
            
            for j, col_value in enumerate(row[2:]):
                letra = letras[j]
                
                if col_value == PARED:
                    continue
                
                letra_id = num+letra

                self.grid[letra_id] = {
                        "h": 0,
                        "pos": [i,j],
                        "value": None,
                    }

                if col_value == AVATAR:
                    self.grid[letra_id]["value"] = AVATAR
                    self.inicio_default = letra_id
                    self.inicio = letra_id
                if col_value == SOLUCION:
                    self.grid[letra_id]["value"] = SOLUCION
                    self.objetivo = letra_id
                if col_value == " ":
                    self.grid[letra_id]["value"] = CAMINO

        self.cargar_distancias()

    def cambiar_inicio(self, id_inicio):
        inicio_letra = posiciones_iniciales_extra[id_inicio]

        if inicio_letra == self.objetivo:
            raise ValueError("Inicio = Objetivo")

        pos = self.grid.get(inicio_letra)

        if pos:
            self.grid[inicio_letra]["value"] = AVATAR
        

        self.grid[self.inicio]["value"] = CAMINO
        self.inicio = inicio_letra

        self.cargar_distancias()

    def cambiar_inicio_sin_cargar_dist(self, id_inicio):
        inicio_letra = posiciones_iniciales_extra[id_inicio]

        if inicio_letra == self.objetivo:
            raise ValueError("Inicio = Objetivo")

        pos = self.grid.get(inicio_letra)

        if pos:
            self.grid[inicio_letra]["value"] = AVATAR
        if not pos:
            # Equivale a nuevo inicio era antes un muro
            pos_nueva = self._letra_a_pos(inicio_letra)
            self.grid[inicio_letra] = {
                        "h": distancia_manhattan(
                            pos_nueva, self.grid[self.objetivo]["pos"]
                        ),
                        "pos": pos_nueva,
                        "value": AVATAR,              
            }

        
        self.grid[self.inicio]["value"] = CAMINO
        self.inicio = inicio_letra


    def cargar_distancias(self):
        """
        Coge el grid y carga las h con distancia manhattan

        manhattan a X
        """
        for punto, propiedades in self.grid.items():
            self.grid[punto]["h"] = distancia_manhattan(
                propiedades["pos"], self.grid[self.objetivo]["pos"]
            )
 
    def vecinos(self, letra_id) -> list:
        """
        En orden [Derecha, Abajo, Izquierda, Arriba]
        """
        elemento = self.grid[letra_id]

        fila, columna = elemento["pos"]
        
        posibles_vecinos = [
            self._pos_a_letra([fila, columna + 1]),
            self._pos_a_letra([fila + 1, columna]),
            self._pos_a_letra([fila, columna - 1]),
            self._pos_a_letra([fila - 1, columna]),
            
        ]

        return [
            pv for pv in posibles_vecinos if pv is not None
        ]

    def _pos_a_letra(self, pos: list) -> str | None:
        pos_x, pos_y = pos

        if pos_x < 0 or pos_y < 0:
            return None

        letra_id = numeros[pos_x]+letras[pos_y]

        if self.grid.get(letra_id) is None:
            return None

        return letra_id

    def _letra_a_pos(self, letra_id):
        num = letra_id[0]
        letra = letra_id[1]

        fila = int(num)
        col = mapa_letras[letra]

        return [fila, col]


    def actualizar(self, letra_id, nueva_h):
        self.grid[letra_id]["h"] = nueva_h

    def get(self, letra_id):
        return self.grid.get(letra_id)

    def h(self, letra_id):
        return self.get(letra_id)["h"]
    
    def pos(self, letra_id):
        return self.get(letra_id)["pos"]

    def valor(self, letra_id):
        return self.get(letra_id)["value"]

    def es_solucion(self, letra_id):
        return self.valor(letra_id) == SOLUCION

    def imprimir_grid_h(self):
            """Imprime el grid con los H"""
            
            print("\n" + "="*70)
            print("GRID CON H ACTUAL \n")
            
            print("     " + "".join([f"{l:<5}" for l in letras]))
            print("   " + "-" * (5 * len(letras)))
            
            for num in numeros:
                fila_str = f"{num} | "
                for letra in letras:
                    letra_id = num + letra
                    
                    if letra_id in self.grid:
                        h_val = self.grid[letra_id]["h"]
                        fila_str += f"{h_val:<4.1f} "
                    else:
                        fila_str += "www  " # Es una pared
                print(fila_str)
            print("="*70 + "\n")
