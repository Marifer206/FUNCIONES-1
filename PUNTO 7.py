import math
import random
import statistics as stats

def promedio(a,b,c,d,e): #cálculo de promedio
    return((a+b+c+d+e)/5)

def mediana(a,b,c,d,e): #cálculo de mediana
    datos = [a,b,c,d,e]
    return (stats.mean(datos))

def promediomultiplicativo(a,b,c,d,e): #cálculo de promedio multiplicativo
    m=(a*b*c*d*e)
    return math.sqrt(m)

def ordenascendente(a,b,c,d,e): #ordenamiento de números de forma ascendente
    lista = [a,b,c,d,e]
    lista.sort()
    return lista

def ordenadescendente(a,b,c,d,e): #ordenamiento de números de forma descendente
    listap = [a,b,c,d,e]
    listap.sort(reverse=True)
    return listap
                
def potencia(a,b,c,d,e): #potencia del máximo número elevado al menor número
    listapb = [a,b,c,d,e]
    return(max(listapb)**min(listapb))

def raizcubicamenor(a,b,c,d,e): #raíz cúbica del menor número
    listapbp = [a,b,c,d,e]
    return((min(listapbp))**(1/3))

def main():
    continuar=8;
    try:
        while continuar==8:
            print("Bienvenid@, ingresa 5 números");
            print("");
            a=float(input("Ingrese el valor de a "))
            print("");
            b=float(input("Ingrese el valor de b "))
            print("");
            c=float(input("Ingrese el valor de c "))
            print("");
            d=float(input("Ingrese el valor de d "))
            print("");
            e=float(input("Ingrese el valor de e "))
            print("");
            print("El promedio de sus números es",promedio(a,b,c,d,e));
            print("");
            print("La mediana de sus números es",mediana(a,b,c,d,e));
            print("");
            print("El promedio multiplicativo de sus números es",promediomultiplicativo(a,b,c,d,e));
            print("");
            print("De menor a mayor, son",ordenascendente(a,b,c,d,e));
            print("");
            print("De mayor a menor, son",ordenadescendente(a,b,c,d,e));
            print("");
            print("La potencia del mayor número elevado al menor número es",potencia(a,b,c,d,e));
            print("");
            print("La raíz cúbica del menor número es",raizcubicamenor(a,b,c,d,e));
            print("");
            continuar=int(input("¿Quiere seguir ejecutando el programa? 8 = SI, 9 = NO "))
            print("");
            print("");
    except:
        print("Error en los datos numéricos");

main() 

