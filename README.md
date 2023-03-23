# :star: FUNCIONES-1 :star:
CUMPLIENDO NUESTRO NUEVO RETO#6

## 1.EJERCICIOS DE CLASE
### EJERCICIO #1
Realice un programa que ingrese dos masas y la distancia que las separa y calcule la fuerza de gravedad entre ellas. Resuelva usando una función.
El programa se hace basado en la ey de la gravitacion universal

$$\text{Ley de la gravitación universal:} \ G=\frac{m_1 \cdot m_2}{r^2}$$

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

## PUNTOS DEL RETO
### PUNTO #1
Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/FRvCmpxx/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
+ Revise como utilizar el valor de pi usando import math y math.pi

```ruby

```

### PUNTO #2
Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/1t4MrzsL/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi

```ruby

```
### PUNTO #3
Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```ruby

```

### PUNTO #4
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```ruby

```

### PUNTO #5
Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

```ruby

```
### PUNTO #6
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```ruby

```
### PUNTO #7
 Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

```ruby

```
### PUNTO #8
 Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

```ruby

```
### PUNTO #9
Consultar qué es y cómo funciona *pip* en python.
Pip es un sistema de gestión de paquetes para Python que permite instalar, actualizar y desinstalar fácilmente paquetes de software escritos en Python. Es muy útil para instalar bibliotecas y módulos de Python que no están incluidos en la biblioteca estándar de Python.

```ruby

```
### PUNTO #10
Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.


```ruby

```
