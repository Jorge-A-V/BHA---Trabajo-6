def distancia_manhattan(punto_a: list, punto_b: list):
    x_a, y_a = punto_a
    x_b, y_b = punto_b

    return abs(x_a - x_b) + abs(y_a - y_b)