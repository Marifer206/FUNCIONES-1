def calcular_vueltas(cantidad_panes, cantidad_leche, cantidad_huevos, monto_pagado)-> int:

    total_compra = ((cantidad_panes * 300) + (cantidad_leche * 3300) + (cantidad_huevos * 350))

    vueltas = monto_pagado - total_compra

    if vueltas < 0:
        return abs(vueltas)
    else:
        return vueltas

if __name__ == '__main__':
    cantidad_panes = int(input("Ingresa la cantidad de panes a comprar: "))
    cantidad_leche = int(input("Ingresa la cantidad de bolsas de leche a comprar: "))
    cantidad_huevos = int(input("Ingresa la cantidad de huevos a comprar: "))
    monto_pagado = int(input("Ingresa el monto que pagarás: "))

    vueltas = calcular_vueltas(cantidad_panes, cantidad_leche, cantidad_huevos, monto_pagado)
    
    if vueltas == 0:
        print("No hay vueltas.")
    elif vueltas < 0:
        print("Lo siento, debes pagar un adicional de:", vueltas)
    else:
        print("Tus vueltas son:", vueltas)