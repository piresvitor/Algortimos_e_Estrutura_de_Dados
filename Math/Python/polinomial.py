import time

def horner(poly, x):
    """
    Avalia um polinômio em um determinado valor de x usando o método de Horner.

    Args:
        poly: Uma lista de coeficientes do polinômio, do termo de maior grau ao constante.
        x: O valor para o qual o polinômio será avaliado.

    Returns:
        O valor do polinômio em x.
    """
    result = poly[0]
    for i in range(1, len(poly)):
        result = result * x + poly[i]
    return result

if __name__ == "__main__":
    start_time = time.time()

    poly = [2, -6, 2, -1]
    x = 3

    polynomial_value = horner(poly, x)

    end_time = time.time()
    time_taken = end_time - start_time

    print(f"Valor do polinômio: {polynomial_value}")
    # Perceba o quão rápido é
    print(f"horner() demorou {time_taken:.6f} segundos para executar")
