# :star: FUNCIONES-1 :star:
CUMPLIENDO NUESTRO NUEVO RETO#6

## 1.EJERCICIOS DEL RETO
1 Realice un programa que ingrese dos masas y la distancia que las separa y calcule la fuerza de gravedad entre ellas. Resuelva usando una función.
El programa se hace basado en la ey de la gravitacion universal

[![image.png](https://i.postimg.cc/cH1LWZc8/image.png)](https://postimg.cc/B8y05rkq)

### CODIGO DEL PROGRAMA

```ruby
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
```

El programa ejecutado se ve asi

[![image.png](https://i.postimg.cc/q7wqfR9y/image.png)](https://postimg.cc/GBBdGc3m)
