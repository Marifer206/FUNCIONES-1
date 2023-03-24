import math

def perimetro(r:float, a:float, b:float) -> float:
    rectangulo = 2 * b + 2 * a
    circulo = 2 * math.pi * r
    return rectangulo + 2 * circulo

def area(r:float, a:float, b:float) -> float:
    rectangulo = a * b
    circulo = math.pi * r**2
    return rectangulo + 2 * circulo

if __name__ == '__main__':
    r = float(input("Ingrese el valor del radio (en cm): "))
    a = float(input("Ingrese la longitud del lado más corto del rectángulo (en cm): "))
    b = float(input("Ingrese la longitud del lado más largo del rectángulo (en cm): "))
    per = perimetro(r, a, b)
    ar = area(r, a, b)
    
    print("El perímetro de la figura es: " + str(per) + " cm.")
    print("El área de la figura es: " + str(ar) + " cm².")