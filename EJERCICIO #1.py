G : float 
G = 6.67384e-11

def calcular_fuerza_gravedad_entre_dos_objetos(masa1, masa2, distancia):
    fuerza = G * (masa1 * masa2) / distancia**2
    return fuerza

if __name__ == "__main__":
    masa1 = float(input("Ingrese la masa en Kilogramos del primer objeto: "))
    masa2 = float(input("Ingrese la masa en Kilogramos del segundo objeto: "))
    distancia = float(input("Ingrese la distancia en metros que los separa: "))

    fuerza_gravedad = calcular_fuerza_gravedad_entre_dos_objetos(masa1, masa2, distancia)

    print("La fuerza de gravedad entre los dos objetos es:", fuerza_gravedad, "Newtons")