def probabilidad_dados(objetivo):
    """
    Calcula la probabilidad de obtener una combinacion especifica al lanzar dos dados.

    Args:
        objetivo (int): La suma de los valores de los dos dados que se desea obtener.

    Returns:
        float: La probabilidad de obtener la combinacion especifica.
    """
    # Contador para almacenar la cantidad de combinaciones validas
    conteo = 0
    
    # Lanzar dos dados y contar la cantidad de veces que la suma de los valores es igual al objetivo
    for dado1 in range(1, 7):  # Itera sobre las caras del primer dado
        for dado2 in range(1, 7):  # Itera sobre las caras del segundo dado
            if dado1 + dado2 == objetivo:  # Verifica si la suma de las caras es igual al objetivo
                conteo += 1  # Incrementa el contador de combinaciones validas
    
    # Calcular la probabilidad como la proporcion de combinaciones validas respecto al total de combinaciones posibles
    total_combinaciones = 6 * 6  # Hay 6 caras en cada dado
    probabilidad = conteo / total_combinaciones
    
    return probabilidad

# Calcular la probabilidad de obtener una suma de 7 al lanzar dos dados
resultado = probabilidad_dados(7)
print("La probabilidad de obtener una suma de 7 al lanzar dos dados es:", resultado)

