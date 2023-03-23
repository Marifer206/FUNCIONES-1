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

:checkered_flag: El programa ejecutado se ve asi

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

:checkered_flag: El programa ejecutado se ve asi

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

#### CODIGO DEL PROGRAMA
```ruby
import math

# Declaramos funcion y damos sus instrucciones
def calcular_volumen(radio_esfera:float, radio_cono:float, altura_cono:float) -> float:
    volumen_esfera = (4/3) * (radio_esfera**3) * math.pi
    volumen_cono = (altura_cono/3) * (radio_cono**2) * math.pi
    return volumen_esfera + volumen_cono    

def calcular_area(radio_esfera:float, radio_cono:float, altura_cono:float) -> float:
    area_esfera = 4 * math.pi * radio_esfera**2
    altura_oblicua = math.sqrt(altura_cono*2 + radio_cono*2)
    area_cono = (math.pi * radio_cono * altura_oblicua) + (math.pi * radio_cono**2)
    return area_esfera + area_cono

if _name_ == '_main_':
    radio_esfera = float(input("Ingrese el radio de la esfera en cm: "))
    radio_cono = float(input("Ingrese el radio del cono en cm: "))
    altura_cono = float(input("Ingrese la altura del cono en cm: "))
    volumen = calcular_volumen(radio_esfera, radio_cono, altura_cono)
    area = calcular_area(radio_esfera, radio_cono, altura_cono)
    
    # Mostramos los resultados
    print("El volumen de la figura es: " + str(volumen) + " cm^3")
    print("El área de la figura es: " + str(area) + " cm^2")
```
:checkered_flag: El programa ejecutado se ve asi



### PUNTO #2
Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/1t4MrzsL/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi

#### CODIGO DEL PROGRAMA
```ruby
import math

# Declaramos funcion y damos sus instrucciones
def perimetro(r:float, a:float, b:float) -> float:
    rectangulo = 2 * b + 2 * a
    circulo = 2 * math.pi * r
    return rectangulo + 2 * circulo

def area(r:float, a:float, b:float) -> float:
    rectangulo = a * b
    circulo = math.pi * r**2
    return rectangulo + 2 * circulo

if _name_ == '_main_':
    r = float(input("Ingrese el valor del radio (en cm): "))
    a = float(input("Ingrese la longitud del lado más corto del rectángulo (en cm): "))
    b = float(input("Ingrese la longitud del lado más largo del rectángulo (en cm): "))
    per = perimetro(r, a, b)
    ar = area(r, a, b)
    
    # Mostramos los resultados
    print("El perímetro de la figura es: " + str(per) + " cm.")
    print("El área de la figura es: " + str(ar) + " cm².")
```
:checkered_flag: El programa ejecutado se ve asi



### PUNTO #3
Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

#### CODIGO DEL PROGRAMA
```ruby

# Declaramos funcion y damos sus instrucciones
def calcular_cantidad_carne_aves():
    peso_gallinas = n_gallinas * 6
    peso_gallos = m_gallos * 7
    peso_pollitos = k_pollitos * 1
    total_peso = peso_gallinas + peso_gallos + peso_pollitos
    return total_peso

if _name_ == '_main_':
    n_gallinas = int(input("Ingrese la cantidad de gallinas: "))
    m_gallos = int(input("Ingrese la cantidad de gallos: "))
    k_pollitos = int(input("Ingrese la cantidad de pollitos: "))
    cantidad_carne = calcular_cantidad_carne_aves()
    
    # Mostramos los resultados
    print("La cantidad de carne de aves es:", cantidad_carne, "kilos")
```

:checkered_flag: El programa ejecutado se ve asi



### PUNTO #4
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

#### CODIGO DEL PROGRAMA
```ruby
# Declaramos funcion y damos sus instrucciones
def calcular_vueltas(cantidad_panes, cantidad_leche, cantidad_huevos, monto_pagado):
    # Calculamos el total de la compra
    total_compra = cantidad_panes * 300 + cantidad_leche * 3300 + cantidad_huevos * 350

    # Calculamos las vueltas o lo que queda debiendo
    vueltas = monto_pagado - total_compra

    if vueltas < 0:
        # Devolvemos el valor de la deuda en lugar de las vueltas
        return abs(vueltas)
    else:
        return vueltas


if _name_ == '_main_':
    cantidad_panes = int(input("Ingresa la cantidad de panes a comprar: "))
    cantidad_leche = int(input("Ingresa la cantidad de bolsas de leche a comprar: "))
    cantidad_huevos = int(input("Ingresa la cantidad de huevos a comprar: "))
    monto_pagado = int(input("Ingresa el monto que pagarás: "))

    vueltas = calcular_vueltas(cantidad_panes, cantidad_leche, cantidad_huevos, monto_pagado)
    
# Mostramos los resultados
    if vueltas == 0:
        print("No hay vueltas.")
    elif vueltas < 0:
        print("Lo siento, debes pagar un adicional de:", vueltas)
    else:
        print("Tus vueltas son:", vueltas)
```
:checkered_flag: El programa ejecutado se ve asi



### PUNTO #5
Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

#### CODIGO DEL PROGRAMA
```ruby

```
### PUNTO #6
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

#### CODIGO DEL PROGRAMA
```ruby

```

:checkered_flag: El programa ejecutado se ve asi



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

:checkered_flag: El programa ejecutado se ve asi



### PUNTO #8
 Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

```ruby

```

### PUNTO #9
Consultar qué es y cómo funciona *pip* en python.

***Consulta Pip:*** 

Es un sistema de gestión de paquetes para Python que permite instalar, actualizar y desinstalar fácilmente paquetes de software escritos en Python. Es muy útil para instalar bibliotecas y módulos de Python que no están incluidos en la biblioteca estándar de Python.

```ruby

```
### PUNTO #10
Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.


```ruby

```
