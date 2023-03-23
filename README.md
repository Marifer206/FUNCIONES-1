# :star: FUNCIONES-1 :star:
CUMPLIENDO NUESTRO NUEVO RETO#6

## 1.EJERCICIOS DEL RETO
### EJERCICIO #1
Realice un programa que ingrese dos masas y la distancia que las separa y calcule la fuerza de gravedad entre ellas. Resuelva usando una función.
El programa se hace basado en la ey de la gravitacion universal

[![image.png](https://i.postimg.cc/cH1LWZc8/image.png)](https://postimg.cc/B8y05rkq)

#### CODIGO DEL PROGRAMA

```ruby
# Declaramos e iniciamos constante
G : float 
G = 6.67384e-11

# Declaramos funcion y damos sus instrucciones
def calcular_fuerza_gravedad_entre_dos_objetos(masa1, masa2, distancia):
    fuerza = G * (masa1 * masa2) / distancia**2
    return fuerza

if __name__ == "__main__":
    masa1 = float(input("Ingrese la masa en Kilogramos del primer objeto: "))
    masa2 = float(input("Ingrese la masa en Kilogramos del segundo objeto: "))
    distancia = float(input("Ingrese la distancia en metros que los separa: "))

    fuerza_gravedad = calcular_fuerza_gravedad_entre_dos_objetos(masa1, masa2, distancia)

# Mostramos el resultado
    print("La fuerza de gravedad entre los dos objetos es:", fuerza_gravedad, "Newtons")
```

El programa ejecutado se ve asi

[![image.png](https://i.postimg.cc/q7wqfR9y/image.png)](https://postimg.cc/GBBdGc3m)

### EJERCICIO #2
Uno de los módulos que trae python es math, hacer un porgrama en Python importando math y usar 5 de las funciones incluidas en este módulo.

#### CODIGO DEL PROGRAMA
```ruby
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

# Mostramos los resultados
print("La potencia de", x, "elevado a", y, "es:", potencia)
print("El seno de", angulo, "grados es:", seno)
print("El valor absoluto de", z, "es:", valor_absoluto)
print(grados, "grados equivalen a", radianes, "radianes")
print("La raíz cuadrada de", numero_raiz, "es:", raiz_cuadrada)
```

El programa ejecutado se ve asi

[![image.png](https://i.postimg.cc/0NxrZhbr/image.png)](https://postimg.cc/TK7R37jX)
