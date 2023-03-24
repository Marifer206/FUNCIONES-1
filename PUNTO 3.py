def calcular_cantidad_carne_aves():
    peso_gallinas = n_gallinas * 6
    peso_gallos = m_gallos * 7
    peso_pollitos = k_pollitos * 1
    total_peso = peso_gallinas + peso_gallos + peso_pollitos
    return total_peso

if __name__ == '__main__':
    n_gallinas = int(input("Ingrese la cantidad de gallinas: "))
    m_gallos = int(input("Ingrese la cantidad de gallos: "))
    k_pollitos = int(input("Ingrese la cantidad de pollitos: "))
    cantidad_carne = calcular_cantidad_carne_aves()
    
    print("La cantidad de carne de aves es:", cantidad_carne, "kilos")