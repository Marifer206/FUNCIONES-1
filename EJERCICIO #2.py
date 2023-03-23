import math

# Pedimos al usuario que introduzca los valores de las variables
x = float(input("Introduce un número para calcular su potencia: "))
y = float(input("Introduce el exponente para calcular la potencia: "))
angulo = float(input("Introduce un ángulo en grados para calcular su seno: "))
z = float(input("Introduce un número para calcular su valor absoluto: "))
grados = float(input("Introduce un ángulo en grados para convertirlo a radianes: "))
numero_raiz = float(input("Introduce un número para calcular su raíz cuadrada: "))

# Utilizamos las funciones del módulo math con las variables introducidas por el usuario
potencia = math.pow(x, y)
raiz_cuadrada = math.sqrt(numero_raiz)
seno = math.sin(math.radians(angulo))
valor_absoluto = math.fabs(z)
radianes = math.radians(grados)

print("La potencia de", x, "elevado a", y, "es:", potencia)
print("La raíz cuadrada de", numero_raiz, "es:", raiz_cuadrada)
print("El seno de", angulo, "grados es:", seno)
print("El valor absoluto de", z, "es:", valor_absoluto)
print(grados, "grados equivalen a", radianes, "radianes")