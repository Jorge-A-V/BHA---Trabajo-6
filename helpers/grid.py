from .heuristicos import distancia_manhattan

PARED = "w"
AVATAR = "A"
SOLUCION = "X"
CAMINO = "C"

posiciones_iniciales_extra = ['2F', '1I', '5H', '5L', '1K', '4B', '3H', '3I', '5C', '5B']

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

        rows = self.grid_texto.split("\n")

        letras = rows[1][2:]
        numeros = ['0','1','2','3','4','5','6']

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
                if col_value == " ":
                    self.grid[letra_id]["value"] = CAMINO

        self.cargar_distancias()

    def cambiar_inicio(self, id_inicio):
        inicio_letra = posiciones_iniciales_extra[id_inicio]
        
        pos = self.grid.get(inicio_letra)

        if pos:
            self.grid[inicio_letra]["value"] = AVATAR
        
        self.grid[self.inicio_default]["value"] = CAMINO
        self.inicio = inicio_letra

        self.cargar_distancias()

    def cargar_distancias(self):
        """
        Coge el grid y carga las h con distancia manhattan
        """
        for punto, propiedades in self.grid.items():
            if propiedades["value"] == AVATAR:
                self.grid[punto]["h"] = 0
            else:
                self.grid[punto]["h"] = distancia_manhattan(
                   propiedades["pos"], self.grid[self.inicio]["pos"]
                )

        


    
