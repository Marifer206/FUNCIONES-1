import math

def calcular_volumen(radio_esfera:float, radio_cono:float, altura_cono:float) -> float:
    volumen_esfera = (4/3) * (radio_esfera**3) * math.pi
    volumen_cono = (altura_cono/3) * (radio_cono**2) * math.pi
    return volumen_esfera + volumen_cono    

def calcular_area(radio_esfera:float, radio_cono:float, altura_cono:float) -> float:
    area_esfera = 4 * math.pi * radio_esfera**2
    altura_oblicua = math.sqrt(altura_cono*2 + radio_cono*2)
    area_cono = (math.pi * radio_cono * altura_oblicua) + (math.pi * radio_cono**2)
    return area_esfera + area_cono

if __name__ == '__main__':
    radio_esfera = float(input("Ingrese el radio de la esfera en cm: "))
    radio_cono = float(input("Ingrese el radio del cono en cm: "))
    altura_cono = float(input("Ingrese la altura del cono en cm: "))
    volumen = calcular_volumen(radio_esfera, radio_cono, altura_cono)
    area = calcular_area(radio_esfera, radio_cono, altura_cono)
    
    print("El volumen de la figura es: " + str(volumen) + " cm^3")
    print("El área de la figura es: " + str(area) + " cm^2")