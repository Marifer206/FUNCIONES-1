def calcular_contagios(contagiados_actuales: int, dias_transcurridos: int) -> int:
    return contagiados_actuales * (2 ** dias_transcurridos)

if __name__ == '__main__':
    contagiados_actuales = int(input("Ingrese el número de contagiados actuales: "))
    dias_transcurridos = int(input("Ingrese el número de días a partir de hoy: "))
    total_contagios = calcular_contagios(contagiados_actuales, dias_transcurridos)
    print(f"El número total de personas contagiadas después de {dias_transcurridos} días es: {total_contagios}")