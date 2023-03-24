def calcular_valor_prestamo(prestamo: float, tasa_interes: float, meses: int) -> float:
    interes = tasa_interes * prestamo / 100
    return prestamo + meses * interes

if __name__ == '__main__':
    prestamo = float(input("Ingrese el valor del préstamo en pesos: "))
    tasa_interes = float(input("Ingrese la tasa de interés en porcentaje: "))
    meses = int(input("Ingrese el número de meses para el préstamo: "))
    valor_prestamo = calcular_valor_prestamo(prestamo, tasa_interes, meses)
    print("El valor a pagar es de: " + str(valor_prestamo))
