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