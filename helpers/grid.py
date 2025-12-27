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
        6 wwwwwwwwwwwww
    """

    def __init__(self):

        self.grid = {}
        self.inicio_default = None

        rows = example.split("\n")

        letras = row[0].split("")[2:]
        numeros = ['0','1','2','3','4','5','6']

        for i, (row, num) in enumerate(zip(rows[1:], numeros)):        
            for j, (col_value, letra) in enumerate(zip(row[2:], letras)):
                if col_value == PARED:
                    continue
                
                self.grid[letra+num] = {
                        "h": 0,
                        "pos": [i,j],
                        "value": None,
                    }

                if col_value == AVATAR:
                    self.grid[letra+num]["value"] = AVATAR
                    self.inicio_default = letra+num
                if col_value == SOLUCION:
                    self.grid[letra+num]["value"] = SOLUCION
                if col_value == " ":
                    self.grid[letra+num]["value"] = CAMINO

    def cambiar_inicio(self, id_inicio):
        inicio_letra = posiciones_iniciales_extra[id_inicio]

        pos = self.grid[inicio_letra]

        if pos:
            self.grid[inicio_letra] = 


        


    
